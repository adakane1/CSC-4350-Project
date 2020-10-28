from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NutritionGoal(models.Model):
    parentUser = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    description = models.TextField()