from django.shortcuts import render
from .models import Questions
# Create your views here.

def questions_list(request):
    questions = Questions.objects.all()
    context = {
        "questions" : questions

    }
    return render(request, 'questans/qlist.html', context)
