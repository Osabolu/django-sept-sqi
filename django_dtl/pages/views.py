from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def contacts(request):
    context = {"my_price": ["billings", "bids"]}
    return render(request, "pages/contacts.html", context)
