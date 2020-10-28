from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    parentUser = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=40)
    date = models.DateTimeField()
    description = models.TextField()