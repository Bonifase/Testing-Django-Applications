from django.urls import path, re_path

from .views import (
    DeleteTaskView,
    HomeView,
    NewTaskView,
    TaskListView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    re_path(r'tasks/(?P<view>.*)$', TaskListView.as_view(), name='dashboard'),
    path('new-task/', NewTaskView.as_view(), name='new_task'),
    path('delete-task/<slug:pk>/', DeleteTaskView.as_view(), name='delete_task'),
    # path('tasks/', TaskListView.as_view(), name='toggle_view'),
]
