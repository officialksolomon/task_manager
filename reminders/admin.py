from django.contrib import admin

from reminders.models import Reminder

# Register your models here.


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
        "description",
        "status",
        "due_date",
    ]
    list_filter = ["name", "owner", "status", "due_date"]
    list_search = ["owner", "status", "due_date"]
