from importlib.abc import ExecutionLoader
from pyexpat import model
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    """
    a ModelForm for a Task instance.
    """
    class Meta:
        exclude = ('px', 'owner', 'complete_time', )
        model = Task
