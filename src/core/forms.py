# Import necessary modules from Django
from django import forms
from .models import User
from django.contrib.auth.password_validation import MinimumLengthValidator

# Define a list of validators, currently only includes MinimumLengthValidator
validators = [MinimumLengthValidator]


# Define a form for user registration
class RegisterForm(forms.ModelForm):
    # Define form fields with their respective attributes
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password = forms.CharField(widget=forms.PasswordInput(), validators=validators)
    email = forms.EmailField()

    # Meta class to link form to User model and define form fields
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        # Initialize form and add CSS classes to fields
        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class': 'form-control'})


# Define a form for user login
class LoginForm(forms.ModelForm):
    # Define form fields with their respective attributes
    password = forms.CharField(widget=forms.PasswordInput())

    # Meta class to link form to User model and define form fields
    class Meta:
        model = User
        fields = ['email', 'password']
