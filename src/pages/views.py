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
    return render(request, "index.html", context)

# def signUp_view(request, *args, **kwargs):
#     return render(request, "signup.html", {})