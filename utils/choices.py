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

class ReminderStatus(models.TextChoices):
    completed = ("completed", "Completed")
    not_completed = ("not-completed", "Not Completed")

class ReminderFrequency(models.TextChoices):
    half_daily = ("half daily", "Half Daily")
    hourly =  ("hourly", "Hourly")
    daily = ("daily", "Daily")
    weekly = ("weekly", "Weekly")
  


class NotificationType(models.TextChoices):
    email = ("email", "E-mail")
    sms = ("sms", "SMS")
