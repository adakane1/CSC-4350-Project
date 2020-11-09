from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

@login_required
def dash_view(request, *args, **kwargs):
    # print(request.user)

    return render(request, "index.html", {})

# def signUp_view(request, *args, **kwargs):
#     return render(request, "signup.html", {})