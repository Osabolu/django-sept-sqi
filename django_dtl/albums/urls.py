from django.urls import path
from . import views

urlpatterns = [
    path("", views.album, name="home"),
    path("album", views.album, name="album"),
]