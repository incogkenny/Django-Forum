# Import necessary modules from Django and the project
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from questans.models import Questions, Answers
from .forms import LoginForm, RegisterForm
from .models import User


# Define a view for the dashboard
class DashboardView(FormView):
    # Define the GET method for the view
    def get(self, request, **kwargs):
        # Initialise a dictionary to hold the content to be rendered
        content = {}
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the user and question objects
            user = request.user
            user.backend = 'django.contrib.core.backends.ModelBackend'
            ques_obj = Questions.objects.all()
            # Add the user and question details to the content dictionary
            content['userdetail'] = user
            content['questions'] = ques_obj
            # Get the answers for the first question and add them to the content dictionary
            ans_obj = Answers.objects.filter(question=ques_obj.first())
            content['answers'] = ans_obj
            # Render the dashboard with the content
            return render(request, 'dashboard.html', content)
        else:
            # If the user is not authenticated, redirect them to the login view
            return redirect(reverse('login-view'))


# Define a view for user registration
class RegisterView(FormView):
    # Use the csrf_exempt decorator to exempt this view from CSRF protection
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Call the parent class's dispatch method
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    # Define the GET method for the view
    def get(self, request, **kwargs):
        # Initialise a dictionary to hold the content to be rendered
        content = {'form': RegisterForm}
        # Render the registration page with the content
        return render(request, 'register.html', content)

    # Define the POST method for the view
    def post(self, request, **kwargs):
        # Initialise a dictionary to hold the content to be rendered
        content = {}
        # Get the form data from the request
        form = RegisterForm(request.POST, request.FILES or None)
        # Check if the form data is valid
        if form.is_valid():
            # Save the form data but don't commit it to the database yet
            save_it = form.save(commit=False)
            # Hash the password and save it to the user object
            save_it.password = make_password(form.cleaned_data['password'])
            # Save the user object to the database
            save_it.save()
            # Log the user in and redirect them to the questions list
            login(request, save_it)
            return redirect(reverse('questions_list'))
        # If the form data is not valid, add the form to the content dictionary
        content['form'] = form
        # Render the registration page with the content
        return render(request, 'register.html', content)


# Define a view for user login
class LoginView(FormView):
    # Initialise a dictionary to hold the content to be rendered
    content = {'form': LoginForm}

    # Use the csrf_exempt decorator to exempt this view from CSRF protection
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Call the parent class's dispatch method
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    # Define the GET method for the view
    def get(self, request, **kwargs):
        # Initialise a dictionary to hold the content to be rendered
        content = {}
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # If the user is authenticated, redirect them to the questions list
            return redirect('questions_list')
        # If the user is not authenticated, add the login form to the content dictionary
        content['form'] = LoginForm
        # Render the login page with the content
        return render(request, 'login.html', content)

    # Define the POST method for the view
    def post(self, request, **kwargs):
        # Initialize a dictionary to hold the content to be rendered
        content = {}
        # Get the email and password from the request
        email = request.POST['email']
        password = request.POST['password']
        # Try to authenticate the user
        try:
            # Get the user object that matches the email
            users = User.objects.filter(email=email)
            # Authenticate the user
            user = authenticate(request, username=users.first().username, password=password)
            # Log the user in and redirect them to the home page
            login(request, user)
            return redirect('/')
        except Exception as e:
            # If the authentication fails, add an error message to the content dictionary
            content = {'form': LoginForm, 'error': 'Unable to login with provided credentials' + str(e)}
            # Render the login page with the content
            return render(request, 'login.html', content)


# Define a view for user logout
class LogoutView(FormView):
    # Define the GET method for the view
    def get(self, request, **kwargs):
        # Log the user out and redirect them to the home page
        logout(request)
        return HttpResponseRedirect('/')
