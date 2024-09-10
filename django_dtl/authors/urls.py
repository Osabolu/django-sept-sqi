from django.urls import path
from . import views

urlpatterns = [
    path("authors-list", views.all_authors, name="all_authors"),
     path("book-signings", views.book_signings, name="book_signings"),

]