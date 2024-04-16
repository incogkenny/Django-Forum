from django.shortcuts import render, get_object_or_404
from .models import Questions, Answers
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from core.models import User
from questans.models import Questions, Answers, QuestionGroups
from .forms import QuestionForm, AnswerForm

# Create your views here.

def questions_list(request):
    content = {}
    user = request.user #Request user data from user app
    user.backend = 'django.contrib.core.backends.ModelBackend'
    ques_obj = Questions.objects.all() #Finds all objects from the Question class
    content['userdetail'] = user
    content['questions'] = ques_obj # Links question data to Homepage HTML
    return render(request, 'questans/qlist.html', content)


def questions_page(request, slug):
    question = get_object_or_404(Questions, slug=slug)
    answers = Answers.objects.filter(question = question.id)

    #Additional information for the Answer form
    form = AnswerForm()
    form.user = request.user
    form.question = question

    context = {'q': question,
               'a' : answers,
               'form' :form}

    #Handles request when the form is submitted
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'questans/qpage.html', context)
    else:
        return render(request, 'questans/qpage.html', context)

def question_form(request):
    user = request.user    #retrieves current user
    form = QuestionForm()  #retrieves the form
    form.user = user       #adds current user as a field
    content = {}
    if request.method == "POST":   #when the form is submitted
        form = QuestionForm(request.POST)   #populates the form with data entered by user
        if form.is_valid():
            form.save()     #method to save the form
            return HttpResponseRedirect('success/')  #redirects to a confirmation page

    #Determines how the page is being rendered
    else:

        content['form'] = QuestionForm()   #takes an empty form
        return render(request, 'questans/qform.html', content)   #and renders it on the page

#Confirmation view
def success(request):
    return render(request,'success.html')



def search_view(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        topics = Questions.objects.filter(title__contains = searched)
        return render(request, "questans/search.html",{"searched":searched, "topics":topics})
    else:
        return render(request, "questans/search.html", {})


def help_view(request):
    return render(request, 'help.html',)

def contact_view(request):
    return render(request, 'contact.html',)