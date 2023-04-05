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
        blank=True,
    )
    description = models.CharField(
        max_length=50,
    )
    frequency = models.CharField(
        max_length=50,
        choices=ReminderFrequency.choices,
        default=ReminderFrequency.daily,
    )
    time = models.TimeField(auto_now_add=True)
    due_date = models.DateField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=ReminderStatus.choices,
        default=ReminderStatus.not_completed,
    )

    def set_owner(self):
        if self.task:
            self.owner = self.task.created_by

    def set_due_date(self):
        if self.task:
            self.due_date = self.task.due_date

    def save(self, *args, **kwargs):
        self.set_owner()
        self.set_due_date()
        super().save(*args, **kwargs)  # Call the real save() method
