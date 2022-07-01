from django.urls import path

from .views import TaskListView, HomeView

# app_name = 'tasks'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='dashboard'),
]