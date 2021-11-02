from django.shortcuts import render, get_object_or_404
from .models import Questions, Answers
# Create your views here.

def questions_list(request):
    questions = Questions.objects.all()
    context = {
        "questions" : questions

    }
    return render(request, 'questans/qlist.html', context)

def questions_page(request, slug):
    content = {}
    if request.user.is_authenticated:
        user = request.user
        user.backend = 'django.contrib.core.backends.ModelBackend'
        ques_obj = Questions.objects.all()
        content['userdetail'] = user
        content['questions'] = ques_obj
        ans_obj = Answers.objects.filter(question=ques_obj.first())
        content['answers'] = ans_obj
        return render(request, 'dashboard.html', content)

    question = get_object_or_404(Questions, slug=slug)
    answers = Answers.objects.filter(question = question)
    question.upvote()
    question.downvote()
    context = {'q': question,
               'a' : answers,

               }
    return render(request, 'questans/qpage.html', context)