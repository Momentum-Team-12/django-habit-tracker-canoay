from django.contrib import admin
from .models import Habit, Tracker, CustomUser

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Habit)
admin.site.register(Tracker)