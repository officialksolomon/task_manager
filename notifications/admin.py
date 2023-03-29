from django.contrib import admin

from notifications.models import Notification




@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["owner",  "message", "type", "sent_at"]
    list_filter = ["owner",  "message", "type"]
    list_search = ["owner",  "message", "type"]
    

   
    
