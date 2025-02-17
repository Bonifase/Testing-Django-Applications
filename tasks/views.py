from re import T
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import RedirectView, TemplateView, CreateView, DeleteView, UpdateView

from rest_framework.permissions import IsAuthenticated

from .models import Task
from .forms import TaskForm
from .mixins import DashboardRedirectMixin

class HomeView(RedirectView):
    """
       Home page. Redirects to login page or task list.
    """
    permanent: bool = True

    def get_redirect_url(self, *args, **kwargs):
        if hasattr(self.request, 'user') and self.request.user.is_active:
            return reverse('dashboard', kwargs={'view':"grid"})
        else:
            return reverse('login')


class TaskListView(TemplateView):
    """
       View class to list logged in users tasks.
       Must be an authenticated user to perform this action.
    """
    template_name = 'dashboard/grid_list.html'
    title = "Tasks"
    list_view = "grid"
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['tasks'] = self.get_queryset()
        context['title'] = self.title
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print(context)

        if context['view'] == "table":
            context['list_view'] = "table"
            self.template_name = 'dashboard/table_list.html'
            return self.render_to_response(context)

        elif context['view'] == "grid":
            context['list_view'] = "grid"
            self.template_name = 'dashboard/grid_list.html'
            return self.render_to_response(context)

        else:
            context['list_view'] = "grid"
            return self.render_to_response(context)


class NewTaskView(DashboardRedirectMixin, CreateView):
    """
       View class to create a new task.
       Must be an authenticated user to perform this action.
       Redirects to the task list view upon creation.
    """
    permission_classes = [IsAuthenticated]
    template_name = 'dashboard/task.html'
    form_class = TaskForm
    title = "New Task"
    # print(dir(form_class))

    def form_valid(self, form):
        task = form.save(commit=False)
        task.owner = self.request.user
        task.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteTaskView(DeleteView):
    """
       View class to delete a task.
       Must be owner of the task to perform this action.
       Redirects to the task list view upon deletion.
    """
    title = "Delete Task"
    model = Task
    pk_url_kwarg = 'task_id'


class TaskView(UpdateView):
    """
       View class to view and edit a task.
       Must be owner of the task to perform this action.
       Redirects to the task list view upon completion.
    """
    template_name = 'dashboard/task.html'
    title = 'Update Task'
    form_class = TaskForm
    pk_url_kwarg = 'task_id'

    def get_queryset(self):
        if hasattr(self.request, 'user') and self.request.user.is_active :
            return Task.objects.filter(owner=self.request.user)
        return Task.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(TaskView, self).get_context_data(*args, **kwargs)
        context['update'] = True
        return context


def toggle_complete(request, task_id):
    """
       Toggles complete status a task.
       If a task with task_id is incomplete, mark complete else mark incomplete.
       Must be owner of the task to perform this action.
    """
    try:
        task = Task.objects.get(pk=task_id, owner=request.user)
    except Task.DoesNotExist:
        return HttpResponseNotFound()

    if task.is_complete:
        task.mark_incomplete()
    else:
        task.mark_complete()

    return HttpResponseRedirect(reverse('dashboard: dashboard'))



