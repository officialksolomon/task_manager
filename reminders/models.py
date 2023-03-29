from django.db import models
import auto_prefetch
from utils.choices import ReminderFrequency, ReminderStatus

from utils.models import NamedTimeBasedModel

# Create your models here.


class Reminder(NamedTimeBasedModel):
    task = auto_prefetch.ForeignKey(
        "task.Task",
        related_name="reminders",
        on_delete=models.CASCADE,
    ) 
    owner = auto_prefetch.ForeignKey(
        "accounts.CustomUser",
        related_name="user_reminders",
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50, choices=ReminderFrequency.choices)
    time = models.TimeField()
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=ReminderStatus.choices)
