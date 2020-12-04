from django.shortcuts import render
from .forms import GoalUpdateForm
from .models import Goal
from profiles.models import Profile

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
        
        if Goal.goal_type == 0:
            request.user.profile.e_goals_complete = False
        if Goal.goal_type == 1:
            request.user.profile.n_goals_complete = False
        if Goal.goal_type == 2:
            request.user.profile.s_goals_complete = False
        else:
            request.user.profile.a_goals_complete = False
        request.user.profile.save()
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
    e = request.user.profile.e_goals_complete
    n = request.user.profile.n_goals_complete
    s = request.user.profile.s_goals_complete
    a = request.user.profile.a_goals_complete

    context = {
        "singleGoal": singleGoal,
        "hasGoals": False,
        "e_goals_complete": e,
        "n_goals_complete": n,
        "s_goals_complete": s,
        "a_goals_complete": a
    }
    # context = (Goal.objects.filter(user=request.user).values())

    e_goals = 0
    n_goals = 0
    s_goals = 0
    a_goals = 0
    for goal in Goal.objects.filter(user=request.user).values():
        print(request.user.profile.e_goals_complete)
        singleGoal.append(goal)
        context["hasGoals"] = True
        if goal["goal_type"] == 0:
            e_goals += 1
            if not goal["complete"]:
                request.user.profile.e_goals_complete = False
            else:
                e_goals -= 1
            if not e_goals:
                request.user.profile.e_goals_complete = True
        elif goal["goal_type"] == 1:
            n_goals += 1
            if not goal["complete"]:
                request.user.profile.n_goals_complete = False
            else:
                n_goals -= 1
            if not n_goals:
                request.user.profile.n_goals_complete = True
        elif goal["goal_type"] == 2:
            s_goals += 1
            if not goal["complete"]:
                request.user.profile.s_goals_complete = False
            else:
                s_goals -= 1
            if not s_goals:
                request.user.profile.s_goals_complete = True
        else:
            a_goals += 1
            if not goal["complete"]:
                request.user.profile.a_goals_complete = False
            else:
                a_goals -= 1
            if not a_goals:
                request.user.profile.a_goals_complete = True
        request.user.profile.save()
    return render(request, "goals/goal_detail.html", context)

@login_required
def goal_delete_view(request, id):
    obj = get_object_or_404(Goal, id=id)
    if request.user == obj.user:
        print('confirming delete from right user...')
        obj.delete()    
    return redirect('goal')

@login_required
def goal_complete_view_from_dash(request, id):
    obj = get_object_or_404(Goal, id=id)
    if request.user == obj.user:
        if obj.complete:
            obj.complete = False
        else:
            obj.complete = True
        obj.save()
    return redirect('dash')

@login_required
def goal_complete_view_from_goals(request, id):
    obj = get_object_or_404(Goal, id=id)
    if request.user == obj.user:
        if obj.complete:
            obj.complete = False
        else:
            obj.complete = True
        obj.save()
    return redirect('goal')