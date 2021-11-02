from django.contrib import admin
from django.urls import path, include
from .views import questions_list, questions_page

urlpatterns = [
    path('', questions_list, name='questions-list'),
    path('question/<str:slug>', questions_page, name='questions_page'),
]