from django.contrib import admin
from django.urls import path, include
from .views import questions_list, questions_page, help_view, contact_view, search_view, question_form, success

urlpatterns = [
    path('', questions_list, name='questions_list'),
    path('question/<str:slug>', questions_page, name='questions_page'),
    path('help/', help_view, name='help_view'),
    path('contact/', contact_view, name='contact_view'),
    path('search/', search_view, name='search_view'),
    path('form/', question_form, name='question_form'),
    path('form/success/', success, name='success'),
]