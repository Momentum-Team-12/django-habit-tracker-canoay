from django import forms
from .models import Habit, Tracker


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'name',
            'goal',
            'unit',
            'goal_description',
        ]


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = [
            'actual_progress',
            'date',
        ]