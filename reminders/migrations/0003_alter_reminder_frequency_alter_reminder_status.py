# Generated by Django 4.1.7 on 2023-04-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_alter_reminder_due_date_alter_reminder_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='frequency',
            field=models.CharField(choices=[('half daily', 'Half Daily'), ('hourly', 'Hourly'), ('daily', 'Daily'), ('weekly', 'Weekly')], default='daily', max_length=50),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('not-completed', 'Not Completed')], default='not-completed', max_length=50),
        ),
    ]