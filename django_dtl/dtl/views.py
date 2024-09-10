from django.shortcuts import render

# Create your views here.
def new_view(request):
    context = {
        "my_name": "McCoy"
    }
    return render(request, "dtl/dtl.html", context)
