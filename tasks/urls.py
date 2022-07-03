from django.urls import re_path, path

from tasks.views import DeleteTaskView, HomeView, NewTaskView, TaskListView

# app_name = 'dashboard'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/tasks/', TaskListView.as_view(), name='dashboard'),
    path('dashboard/new-task/', NewTaskView.as_view(), name='new_task'),
    path('dashboard/delete-task/<int:task_id>/', DeleteTaskView.as_view(), name='delete_task'),
]