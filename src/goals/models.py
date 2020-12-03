from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User
import datetime
from datetime import datetime as dt

def relativeDate(numDays):
    return dt.now() + datetime.timedelta(days=numDays)

def tomorrow():
    return dt.now() + datetime.timedelta(days=1)

DATES = {
    (relativeDate(1), "tomorrow"),
    (relativeDate(7), "1 week"),
    (relativeDate(14), "2 weeks"),
    (relativeDate(30), "1 month"),
}

GOAL_TYPE = {
    (0,"Exercise"),
    (1,"Nutrition"),
    (2,"Sleep"),
    (3,"Appointment")
}

# Create your models here.
class Goal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.IntegerField(choices=GOAL_TYPE, default=0)
    date = models.DateTimeField(default=tomorrow)
    description = models.TextField(blank=False, max_length=30)
    complete = models.BooleanField(default=False)