# Generated by Django 4.0.4 on 2022-05-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_rename_unit_habit_measurement_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='goal_category',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Professional', 'Professional'), ('For Fun!', 'For Fun!')], default='Personal', max_length=15),
        ),
    ]
