from django.shortcuts import get_object_or_404

from .models import Task


class DashboardRedirectMixin(object):
    """
    Resolves a success URL for a view that redirects to the dashboard.
    """
    def get_success_url(self):
        from django.urls import reverse
        return reverse('dashboard', kwargs={'view':"grid"})


class TaskOwnerMixin(object):
    """
    Ensures that the current logged in user owns the specified task ID before
    performing an action on a task.
    """
    def post(self, request, task_id=None, *args, **kwargs):
        if task_id:
            get_object_or_404(Task, pk=task_id, owner=request.user)

        return super(TaskOwnerMixin, self).post(request, *args, **kwargs)

