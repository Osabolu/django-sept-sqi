from django.urls import path
from . import views

urlpatterns = [
    path("authors-list/", views.all_authors, name="all_authors"),
    path("book-signings/", views.book_signings, name="book_signings"),
    path("new-authors/", views.new_authors, name="new_authors"),
]
