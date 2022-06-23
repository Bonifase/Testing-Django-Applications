from django.db import models
from django.conf import settings
from django.utils import timezone


class TaskManager(models.Manager):

    def get_queryset(self):
        queryset = super(TaskManager, self).get_queryset()
        return queryset.order_by('complete_time', 'due_date')


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.  CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)
    complete_time = models.DateTimeField(null=True, blank=True)

    objects: TaskManager()

    @property
    def is_complete(self):
        """
            Returns True if the task has been completed successfully before the due date.
        """
        return bool(self.complete_time and self.complete_time < timezone.now())

    @property
    def due_soon(self):
        """
            Returns True if the task is due within two days
        """
        min_due = timezone.now() + timezone.timedelta(days=2)
        return bool(self.due_date and self.due_date < min_due)

    def mark_complete(self, commit=True):
        """
            Marks a task as complete by saving the current UTC timestamp in complete_time.
        """
        self.complete_time = timezone.now()
        if commit:
            self.save()

    def mark_incomplete(self, commit=True):
        """
            Marks a task as incomplete by saving None in complete_time.
        """
        self.complete_time = None
        if commit:
            self.save()
          
