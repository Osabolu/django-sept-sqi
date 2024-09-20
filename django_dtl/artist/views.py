from django.shortcuts import render

from . models import Artist
from  albums.models import Record
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, "artist_app/home.html")

def all_artist(request):
    return render(request, "artist_app/artist.html")

def review(request):
    return render(request, "artist_app/review.html")

def new_artist(request):
    new_artists = Artist.objects.all()
    new_records = Record.objects.all()




    context = {
        "new_artists": new_artists,
        "new_records": new_records,
    }
    return render(request, "artist_app/new-artist.html", context)
