from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

HEIGHT_OPTIONS = (
    (53,"4'5\""),
    (54,"4'6\""),
    (55,"4'7\""),
    (56,"4'8\""),
    (57,"4'9\""),
    (58,"4'10\""),
    (59,"4'11\""),
    (60,"5'0\""),
    (61,"5'1\""),
    (62,"5'2\""),
    (63,"5'3\""),
    (64,"5'4\""),
    (65,"5'5\""),
    (66,"5'6\""),
    (67,"5'7\""),
    (68,"5'8\""),
    (69,"5'9\""),
    (70,"5'10\""),
    (71,"5'11\""),
    (72,"6'0\""),
    (73,"6'1\""),
    (74,"6'2\""),
    (75,"6'3\""),
    (76,"6'4\""),
    (77,"6'5\""),
    (78,"6'6\""),
    (79,"6'7\""),
    (80,"6'8\""),
)

EXERCISE_LEVEL_OPTIONS = (
    (0,"Barely Exercise"),
    (1,"Exercise Once In a While"),
    (2,"Exercise Once a Week"),
    (3,"Exercise 2-3 Times a Week"),
    (4,"Exercise Daily"),
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True, unique=True)

    age = models.IntegerField(null=True, blank=True, default=18)
    height = models.IntegerField(choices=HEIGHT_OPTIONS, default=65, blank=True)
    weight = models.IntegerField(default=150, blank=True)
    avg_sleep = models.IntegerField(default=8, blank=True)
    exercise_level = models.IntegerField(choices=EXERCISE_LEVEL_OPTIONS, default=2, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        foo = Profile(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()