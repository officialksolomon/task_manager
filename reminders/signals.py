from django.db.models.signals import post_save
from django.dispatch import receiver
from reminders.models import Reminder
from task.models import Task


@receiver(post_save, sender=Task)
def create_default_task_reminders(sender, instance, **kwargs):
    Reminder.objects.create(
        task=instance,
        name="Automatic Reminder",
        description="Reminder Created automatically for each task.",
    )
