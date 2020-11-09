# Generated by Django 3.1.2 on 2020-11-09 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0007_auto_20201109_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date',
            field=models.DateTimeField(choices=[(datetime.datetime(2020, 11, 23, 19, 41, 50, 68959), '2 weeks'), (datetime.datetime(2020, 11, 10, 19, 41, 50, 68944), 'tomorrow'), (datetime.datetime(2020, 11, 16, 19, 41, 50, 68958), '1 week'), (datetime.datetime(2020, 12, 9, 19, 41, 50, 68960), '1 month')]),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(1, 'Nutrition'), (3, 'Appointment'), (2, 'Sleep'), (0, 'Exercise')], default=0),
        ),
    ]