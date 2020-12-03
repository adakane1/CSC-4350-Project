# Generated by Django 3.1.2 on 2020-12-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0029_auto_20201201_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(0, 'Exercise'), (3, 'Appointment'), (2, 'Sleep'), (1, 'Nutrition')], default=0),
        ),
    ]