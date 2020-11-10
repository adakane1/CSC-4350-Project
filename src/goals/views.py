from django.shortcuts import render
from .forms import GoalUpdateForm
from .models import Goal

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

def goal_create_view(request):
    form = GoalUpdateForm(request.POST or None)

    if form.is_valid():
        Goal = form.save(commit=False)
        Goal.user = request.user
        Goal = Goal.save()
        return redirect('dash')
    context = {
        'form': form
    }

    return render(request, "goals/goal_create.html", context)