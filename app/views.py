from django.shortcuts import render

# Create your views here.


def home_page(request):
    context = {}
    return render(request, "index.html", context)


def login(request):
    context = {}
    return render(request, "login.html", context)


def register(request):
    context = {}
    return render(request, "reg.html", context)
