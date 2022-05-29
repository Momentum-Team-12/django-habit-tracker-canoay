from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, Tracker, CustomUser
from .forms import HabitForm, TrackerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "habit/list_habits.html")

@login_required
def list_habits(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, "habit/list_habits.html",
                  {"habits":habits})

@login_required
def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    date_tracked = Tracker.objects.filter(habit=habit)
    return render(request, "habit/habit_detail.html", {"habit": habit, "date_tracked": date_tracked})

@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, "Congratulations on starting a new habit!")
            return redirect("habit_detail", pk=habit.pk)

    else:
        form = HabitForm()

    return render(request, "habit/add_habit.html", {"form": form})




def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habit/edit_habit.html", {
        "form": form,
        "habit": habit
    })


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method =='POST':
        habit.delete()
        return redirect(to='list_habits')

    return render(request, "habit/delete_habit.html", {"habit": habit})