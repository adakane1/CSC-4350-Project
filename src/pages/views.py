from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from goals.models import Goal
# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

@login_required
def dash_view(request, *args, **kwargs):
    singleGoal = []
    context = {
        "singleGoal": singleGoal,
        "hasGoals": False
    }
    # context = (Goal.objects.filter(user=request.user).values())
    for goal in Goal.objects.filter(user=request.user).values():
        singleGoal.append(goal)
        context["hasGoals"] = True
    return render(request, "index.html", context)

# def signUp_view(request, *args, **kwargs):
#     return render(request, "signup.html", {})