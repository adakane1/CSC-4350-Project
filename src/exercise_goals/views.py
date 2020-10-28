from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ExerciseGoalForm

from .models import ExerciseGoal
# Create your views here.

def exercise_goal_create_view(request):
    return