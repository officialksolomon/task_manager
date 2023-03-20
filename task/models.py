import auto_prefetch
from django.db import models

from utils.models import NamedTimeBasedModel, TimeBasedModel


class Task(NamedTimeBasedModel):
    description = models.CharField(max_length=150)
    status = auto_prefetch.ForeignKey(
        "accounts.TaskStatus", related_name="tasks", on_delete=models.CASCADE
    )
    category = auto_prefetch.ForeignKey(
        "accounts.TaskCategory", related_name="tasks", on_delete=models.CASCADE
    )
    due_date = models.DateField()
    comments = models.CharField(max_length=150)
    assigned_to = auto_prefetch.ForeignKey(
        "accounts.CustomUser", related_name="tasks", on_delete=models.CASCADE
    )
    created_by = auto_prefetch.ForeignKey(
        "accounts.CustomUser", related_name="tasks", on_delete=models.CASCADE
    )
    modified_by = auto_prefetch.ForeignKey(
        "accounts.CustomUser", on_delete=models.CASCADE
    )


class TaskStatus(NamedTimeBasedModel):
    class Meta:
        verbose_name_plural = "Task Statuses"


class TaskCategory(NamedTimeBasedModel):
    class Meta:
        verbose_name_plural = "Task Categories"


class TaskComments(TimeBasedModel):
    content = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Task Comments"
