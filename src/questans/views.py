# Import necessary modules from Django and the project
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .forms import QuestionForm, AnswerForm
from .models import Questions, Answers


# Define a view for the questions list
def questions_list(request):
    # Initialise a dictionary to hold the content to be rendered
    content = {}
    # Get the user and question objects
    user = request.user
    user.backend = 'django.contrib.core.backends.ModelBackend'
    ques_obj = Questions.objects.all()
    # Add the user and question details to the content dictionary
    content['userdetail'] = user
    content['questions'] = ques_obj
    # Render the questions list with the content
    return render(request, 'questans/qlist.html', content)


# Define a view for a specific question page
def questions_page(request, slug):
    # Get the question and answers objects
    question = get_object_or_404(Questions, slug=slug)
    answers = Answers.objects.filter(question=question.id)
    # Initialise the answer form
    form = AnswerForm()
    form.user = request.user
    form.question = question
    # Initialise a dictionary to hold the content to be rendered
    context = {'q': question, 'a': answers, 'form': form}
    # Handle the form submission
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'questans/qpage.html', context)
    else:
        return render(request, 'questans/qpage.html', context)


# Define a view for the question form
def question_form(request):
    # Get the user object
    user = request.user
    # Initialise the question form
    form = QuestionForm()
    form.user = user
    # Initialise a dictionary to hold the content to be rendered
    content = {}
    # Handle the form submission
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success/')
    else:
        content['form'] = QuestionForm()
        return render(request, 'questans/qform.html', content)


# Define a view for the success page
def success(request):
    return render(request, 'success.html')


# Define a view for the search page
def search_view(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        topics = Questions.objects.filter(title__contains=searched)
        return render(request, "questans/search.html", {"searched": searched, "topics": topics})
    else:
        return render(request, "questans/search.html", {})


# Define a view for the help page
def help_view(request):
    return render(request, 'help.html', )


# Define a view for the contact page
def contact_view(request):
    return render(request, 'contact.html', )
