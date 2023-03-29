import auto_prefetch
from django.db import models

# local
from utils.models import NamedTimeBasedModel, TimeBasedModel
from utils.choices import NotificationType

# Create your models here.
class Notification(TimeBasedModel):
    owner = auto_prefetch.ForeignKey(
        "accounts.CustomUser",
        related_name="user_notifications",
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    type = models.CharField(max_length=20, choices=NotificationType.choices)
    sent_at = models.DateTimeField(auto_now=True)



