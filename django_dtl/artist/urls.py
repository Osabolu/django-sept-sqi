from django.urls import path
from . import views

urlpatterns = [
    path("art/", views.all_artist, name="all_artist"),
    path("all-art/", views.new_artist, name="new_artist"),
    path("home/", views.home, name="home"),
    path("review/", views.review, name="review"),

]