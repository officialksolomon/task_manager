# Generated by Django 4.1.7 on 2023-03-24 15:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeamMembers',
            new_name='TeamMember',
        ),
    ]
