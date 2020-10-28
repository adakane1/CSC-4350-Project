from django import forms

from .models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'firstName',
            'lastName',
            'email',
            'age',
            'height',
            'weight',
            'avg_sleep',
            'exercise_level'
        ]
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'weight': 'Weight (lbs)',
            'avg_sleep': 'Average Hours of Sleep per Night'
        }

        