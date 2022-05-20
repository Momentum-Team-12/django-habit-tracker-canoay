from django.shortcuts import render
from .models import Habit, CustomUser, Tracker

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/list_books.html")