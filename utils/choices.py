from django.db import models
from django.utils import timezone


class TaskStatus(models.TextChoices):
    not_started = ("not started", "Not Started")
    in_progress = ("in progress", "In Progress")
    completed = ("completed", "Completed")


class TaskPriority(models.TextChoices):
    normal = ("normal", "Normal")
    low = ("low", "Low")
    high = ("high", "High")
