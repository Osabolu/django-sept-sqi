from django.shortcuts import render


# Create your views here.
def new_view(request):
    context = {
        "my_name": "McCoy",
        "is_dark": True,
        "students": [
            "Abdul",
            "Joseph",
            "Dr. Gafar",
            "Sam",
            "Gbemisola",
            "Emmanuel",
            "Solomon",
            "Dr. Shina",
        ],
    }
    return render(request, "dtl/dtl.html", context)
