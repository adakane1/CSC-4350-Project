from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt
from datetime import timedelta as td

currentTime = dt.now

def relativeDate(numDays):
    if numDays > 0:
        return currentTime + td(days=numDays)
    if numDays < 0:
        return currentTime - td(days=numDays)
    else:
        return currentTime

# Create your models here.
class ExerciseGoal(models.Model):
    parentUser = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    createdDate = models.DateTimeField(default=relativeDate(0), editable=False)
    # deadline = models.DateTimeField(default=relativeDate(1), blank=False)