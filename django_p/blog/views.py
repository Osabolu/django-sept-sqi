from django.shortcuts import render

# Create your views here.

from django.urls import path
from blog import views

urlpatterns = [
    path("about/", views.about, name="about"),
]
