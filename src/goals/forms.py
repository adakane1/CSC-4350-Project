from django import forms

from .models import Goal

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'

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
        widgets = {
            'date': DateTimeInput(attrs={'type': 'datetime'})
        }

        