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
    name             = models.CharField(max_length=300)
    goal             = models.IntegerField(default=0)
    goal_description = models.TextField(max_length=1000, null=True, blank=True)
    user             = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True, related_name="habits" )
    measurement_unit = models.CharField(max_length=100)
    created_at       = models.DateTimeField(auto_now_add=True)
    start_date       = models.DateField(null=True, blank=True)

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





