from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def chatroom(request):
    return HttpResponse("<h3>welcome to our chatroom page<h/>")
