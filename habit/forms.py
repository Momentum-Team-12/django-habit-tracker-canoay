from django import forms
from .models import Habit, Tracker


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'name',
            'goal',
            'measurement_unit',
            'goal_category',
            'start_date',
            'goal_description',
        ]


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = [
            'habit',
            'actual_progress',
            'tracked_date',
        ]