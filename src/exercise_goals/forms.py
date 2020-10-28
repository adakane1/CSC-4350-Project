from django import forms

from .models import ExerciseGoal

class ExerciseGoalForm(forms.ModelForm):
    class Meta:
        model = ExerciseGoal
        fields = [
            'goal',
            'createdDate'
        ]
        labels = {
            
        }