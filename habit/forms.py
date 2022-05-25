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
            'start_date',
        ]


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = [
            'habit',
            'actual_progress',
            'date',
        ]