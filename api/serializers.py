from rest_framework import serializers
from  habit.models import Habit, Tracker, CustomUser


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('pk', 'name', 'goal', 'goal_description', 'measurement_unit', 'start_date', 'goal_category' )


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ( 'pk', 'habit', 'actual_progress', 'tracked_date')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('pk', 'username')


