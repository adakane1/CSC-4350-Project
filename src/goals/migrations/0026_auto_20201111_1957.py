# Generated by Django 3.1.2 on 2020-11-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0025_auto_20201111_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(0, 'Exercise'), (1, 'Nutrition'), (3, 'Appointment'), (2, 'Sleep')], default=0),
        ),
    ]
