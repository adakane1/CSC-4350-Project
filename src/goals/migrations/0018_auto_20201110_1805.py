# Generated by Django 3.1.2 on 2020-11-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0017_auto_20201110_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(1, 'Nutrition'), (0, 'Exercise'), (3, 'Appointment'), (2, 'Sleep')], default=0),
        ),
    ]
