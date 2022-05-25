from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, Tracker
# from .forms import HabitForm, TrackerForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "habit/list_habits.html")

@login_required
def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habit/list_habits.html",
                  {"habits":habits})

