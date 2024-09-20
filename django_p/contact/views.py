from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def contact(request):
    return HttpResponse("<h1>contact us eachoneteachone<h1/>")


def email(request):
    return HttpResponse("send us an email at each.one@gmail.com")
