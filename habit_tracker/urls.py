"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from habit import views as habit_views 
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', habit_views.list_habits, name='list_habits'),
    path('habit/<int:pk>', habit_views.habit_detail, name='habit_detail'),
    path('habit/add_habit/', habit_views.add_habit, name='add_habit'),
    path('habit/<int:pk>/edit/', habit_views.edit_habit, name = 'edit_habit'),
    path('habit/<int:pk>/delete/', habit_views.delete_habit, name='delete_habit'),
    path('accounts/logout/', habit_views.list_habits, name ='logout'),
    path('habit/<int:pk>/create_record', habit_views.create_record, name='create_record'),

#api paths - easier for me to follow along with!
    path('api-auth/', include('rest_framework.urls')),
    path('api/habit', api_views.HabitListView.as_view(), name = 'api_habit_list'),
    path('api/habit/<int:pk>', api_views.HabitDetailView.as_view(), name='api_habit_detail'),
    path('api/tracker', api_views.TrackerListView.as_view(), name = 'api_tracker_list'),
    path('api/tracker/<int:pk>', api_views.TrackerDetailView.as_view(), name = 'api_tracker_detail'),
    path('api/user', api_views.CustomUserListView.as_view(), name = 'api_user_list'),
    path('api/user/<int:pk>', api_views.CustomUserDetailView.as_view(), name = 'api_user_detail'),
]
