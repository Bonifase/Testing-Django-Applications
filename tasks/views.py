
import re
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView

from .models import Task

class Home(RedirectView):
    """
       Home page. Redirects to login page or task list.
    """
    permanent: bool = True

    def get_redirect_url(self, *args, **kwargs):
        if hasattr(self.request, 'user') and self.request.user.is_active:
            return reverse('dashboard')
        else:
            return reverse('login')


class TaskListView(TemplateView):
    template_name = 'dashboard/tasklist.html'
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['task'] = self.get_queryset()
        return context
        
    