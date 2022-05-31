from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.



class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"


class Habit(models.Model):
    PERSONAL         = 'Personal'
    PROFESSIONAL     = 'Professional'
    FUN              = 'For Fun!'
    GOAL_CATEGORY = [
        (PERSONAL, 'Personal'),
        (PROFESSIONAL, 'Professional'),
        (FUN, 'For Fun!'),
    ]
    name             = models.CharField(max_length=300)
    goal             = models.IntegerField(default=0)
    goal_description = models.TextField(max_length=1000, null=True, blank=True)
    user             = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True, related_name="habits" )
    measurement_unit = models.CharField(max_length=100)
    created_at       = models.DateTimeField(auto_now_add=True)
    start_date       = models.DateField(help_text="Please enter date as MM/DD/YYYY")
    goal_category    = models.CharField( max_length=15, choices=GOAL_CATEGORY, default=PERSONAL,)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tracker(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, null=True, blank=True, related_name='trackers')
    actual_progress = models.IntegerField(default=0)
    tracked_date = models.DateTimeField(default=datetime.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['habit', 'tracked_date'], name="daily_record_limit"
            )
        ]





