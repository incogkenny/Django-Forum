from django.contrib import admin
from django.urls import path, include
from .views import questions_list

urlpatterns = [
    path('', questions_list, name='questions-list'),
]