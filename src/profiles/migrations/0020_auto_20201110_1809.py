# Generated by Django 3.1.2 on 2020-11-10 18:09

import datetime
from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20201110_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date',
            field=models.DateTimeField(choices=[(datetime.datetime(2020, 12, 10, 18, 9, 57, 738800), '1 month'), (datetime.datetime(2020, 11, 11, 18, 9, 57, 738784), 'tomorrow'), (datetime.datetime(2020, 11, 17, 18, 9, 57, 738798), '1 week'), (datetime.datetime(2020, 11, 24, 18, 9, 57, 738799), '2 weeks')], default=profiles.models.tomorrow),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(3, 'Appointment'), (2, 'Sleep'), (1, 'Nutrition'), (0, 'Exercise')], default=0),
        ),
    ]