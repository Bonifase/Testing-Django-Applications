from unittest import TestCase
from tasks.models import Task
from django.utils import timezone


class TaskModelTestCase(TestCase):

    def test_complete_model_is_complete(self):
        target = Task()
        target.complete_time = timezone.now() - timezone.timedelta(days=1)

        self.assertTrue(target.is_complete)

    def test_incomplete_model_is_incomplete(self):
        target = Task()
        target.complete_time = None

        self.assertFalse(target.is_complete)

    def test_future_complete_model_is_incomplete(self):
        target = Task()
        target.complete_time = timezone.now() + timezone.timedelta(days=1)

        self.assertFalse(target.is_complete)

    def test_due_soon_model_is_due_soon(self):
        target = Task()
        target.due_date = timezone.now() + timezone.timedelta(days=1)

        self.assertTrue(target.due_soon)

    def test_not_due_soon_model_is_not_due_soon(self):
        target = Task()
        target.due_date = timezone.now() + timezone.timedelta(days=3)

        self.assertFalse(target.due_soon)

    def test_no_due_soon_model_is_not_due_soon(self):
        target = Task()
        target.due_date = None

        self.assertFalse(target.due_soon)

    def test_mark_complete_model_marks_complete(self):
        target = Task()
        target.complete_time = None
        self.assertFalse(target.is_complete)

        target.mark_complete(commit=False)
        self.assertTrue(target.is_complete)

    def test_mark_incomplete_model_marks_incomplete(self):
        target = Task()
        target.complete_time = timezone.now()
        self.assertTrue(target.is_complete)

        target.mark_incomplete(commit=False)
        self.assertFalse(target.is_complete)

