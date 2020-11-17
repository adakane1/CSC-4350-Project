from django import forms

from .models import Goal

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GoalUpdateForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            'goal_type',
            'date',
            'description'
        ]
        labels = {
            'goal_type' : 'Goal Type',
            'date' : 'Complete By',
            'description' : 'GOAL'
        }

        