from csv import Sniffer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, Tracker, CustomUser
from .forms import HabitForm, TrackerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError


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
    return render(request, "habit/habit_detail.html", {"habit": habit, })

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

@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method =='POST':
        habit.delete()
        return redirect(to='list_habits')

    return render(request, "habit/delete_habit.html", {"habit": habit})

@login_required
def create_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method =='GET':
        form = TrackerForm()
        error_msg = None
    else:
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            tracked_date = form.save(commit=False)
            tracked_date.habit = habit
            try:
                tracked_date.save()
                error_msg = None
                messages.success(request, "Another day down!")
                return redirect(to="habit_detail", pk=habit.pk)
            except IntegrityError as error:
                error_msg = "Only one record can exist per date."
    
    return render(request, "habit/create_record.html", {"form":form, "habit":habit, "pk":pk})


@login_required
def edit_record(request, pk):
    tracked_date = get_object_or_404(Tracker, pk=pk)
    if request.method == 'GET':
        form = TrackerForm(instance=tracked_date)
    else:
        form = TrackerForm(data=request.POST, instance=tracked_date)
        if form.is_valid():
            form.save()
            return redirect(to='habit_detail', pk=tracked_date.pk)

    return render(request, "habit/edit_record.html", {
        "form": form,
        "tracked_date": tracked_date},)


@login_required
def delete_record(request, pk):
    tracked_date = get_object_or_404(Tracker, pk=pk)
    if request.method =='POST':
        tracked_date.delete()
        return redirect(to='habit_detail')

    return render(request, "habit/delete_record.html", {"tracked_date": tracked_date})

