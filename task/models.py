import auto_prefetch
from django.db import models

from utils.models import (
    NamedTimeBasedModel,
    TimeBasedModel,
)

from utils.choices import TaskStatus  # type: ignore


class Task(NamedTimeBasedModel):
    description = models.CharField(max_length=150)
    board = auto_prefetch.ForeignKey(
        "task.TaskBoard",
        related_name="board_tasks",
        on_delete=models.CASCADE,
    )
    priority = auto_prefetch.ForeignKey(
        "task.TaskPriority",
        related_name="priority_task",
        on_delete=models.CASCADE,
    )
    team = auto_prefetch.ForeignKey(
        "team.Team",
        related_name="team_tasks",
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=50, choices=TaskStatus.choices)  # type: ignore
    assigned_to = auto_prefetch.ForeignKey(
        "accounts.CustomUser",
        related_name="assigned_tasks",
        on_delete=models.CASCADE,
    )

    category = auto_prefetch.ForeignKey(
        "task.TaskCategory",
        related_name="category_tasks",
        on_delete=models.CASCADE,
    )
    due_date = models.DateField()
    created_by = auto_prefetch.ForeignKey(
        "accounts.CustomUser",
        related_name="user_tasks",
        on_delete=models.CASCADE,
    )


class TaskBoard(NamedTimeBasedModel):
    description = models.CharField(max_length=150)
    created_by = auto_prefetch.ForeignKey(
        "accounts.CustomUser",
        related_name="user_boards",
        on_delete=models.CASCADE,
    )


class TaskPriority(NamedTimeBasedModel):
    level = models.PositiveIntegerField()

    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Task Priorities"

    def __str__(self):
        return self.name


class TaskCategory(NamedTimeBasedModel):
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Task Categories"


class TaskComment(TimeBasedModel):
    task = auto_prefetch.ForeignKey(
        "task.Task",
        related_name="comments",
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=50)
