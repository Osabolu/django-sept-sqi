from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "album/home.html")

def album(request):
    return render(request, "album/albums.html")
