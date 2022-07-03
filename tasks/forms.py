from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    """
    a ModelForm for a Task instance.
    """
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Task title goes here...'}
        )
        self.fields["description"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Task description goes here...'}
        )
        self.fields["due_date"].widget.input_type = "date"
        self.fields["due_date"].widget.attrs.update(
            {'class': 'form-control', 'data-provide': 'datepicker'}
        )

    class Meta:
        exclude = ('px', 'owner', 'complete_time', )
        model = Task
