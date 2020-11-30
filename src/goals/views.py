from django.shortcuts import render
from .forms import GoalUpdateForm
from .models import Goal

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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

@login_required
def goal_detail_view(request):
    print((Goal.objects.filter(user=request.user).values()))
    singleGoal = []
    context = {
        "singleGoal": singleGoal,
        "hasGoals": False
    }
    # context = (Goal.objects.filter(user=request.user).values())
    for goal in Goal.objects.filter(user=request.user).values():
        singleGoal.append(goal)
        context["hasGoals"] = True
    for i in singleGoal:
        print("Goal:")
        print(i)
        print(type(i))
        print()
    return render(request, "goals/goal_detail.html", context)

def goal_delete_view(request, id):
    obj = get_object_or_404(Goal, id=id)
    obj.delete()
    return redirect('goal')