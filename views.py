from django.shortcuts import render


# Create your views here.


def home(request):
    print(l[2])
    return render(request, "home.html", {})
