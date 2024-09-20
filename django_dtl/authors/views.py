from django.shortcuts import render
from .models import Author
from datetime import datetime
from library.models import Book


def all_authors(request):

    return render(request, "authors/all_authors.html")


def book_signings(request):
    return render(request, "authors/book_signings.html")


def new_authors(request):
    #all authors
    all_authors = Author.objects.all()
    #all books
    all_books = Book.objects.all()
    #sorting of authors using birthdate in descending order
    sorted_authors = Author.objects.order_by("-birth_date")
    #books written by darlyn
    darlyn = Author.objects.get(first_name="Darlyn", last_name="Billy")
    darlyn_book = Book.objects.filter(author=darlyn)
    #books before 1999
    year_1999 = datetime(1999, 1, 1)
    old_book = Book.objects.filter(published_on__lt=year_1999)
    #all authors
    all_authors = Author.objects.all()
    #all books
    books = Book.objects.all()
    
    #context variable holds content(s) to render on html for view
    context = {
        "all_authors": all_authors,
        "all_books": all_books,
        "sorted_authors": sorted_authors,
        "darlyn_book": darlyn_book,
        "darlyn": darlyn,
        "old_book": old_book,
        "books":books,
    }
    return render(request, "authors/new-authors.html", context)