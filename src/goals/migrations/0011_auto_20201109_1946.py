# Generated by Django 3.1.2 on 2020-11-09 19:46

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import goals.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0010_auto_20201109_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date',
            field=models.DateTimeField(choices=[(datetime.datetime(2020, 12, 9, 19, 46, 51, 97047), '1 month'), (datetime.datetime(2020, 11, 10, 19, 46, 51, 97023), 'tomorrow'), (datetime.datetime(2020, 11, 16, 19, 46, 51, 97043), '1 week'), (datetime.datetime(2020, 11, 23, 19, 46, 51, 97045), '2 weeks')], default=goals.models.tomorrow),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(0, 'Exercise'), (1, 'Nutrition'), (2, 'Sleep'), (3, 'Appointment')], default=0),
        ),
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]