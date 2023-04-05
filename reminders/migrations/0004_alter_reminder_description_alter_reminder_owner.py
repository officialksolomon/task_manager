# Generated by Django 4.1.7 on 2023-04-04 22:42

import auto_prefetch
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reminders', '0003_alter_reminder_frequency_alter_reminder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='description',
            field=models.CharField(default='Automatic Reminder', max_length=50),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='owner',
            field=auto_prefetch.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reminders', to=settings.AUTH_USER_MODEL),
        ),
    ]
