# Generated by Django 4.1.7 on 2023-04-04 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_task_board_alter_task_category_alter_task_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), ('completed', 'Completed')], default='in progress', max_length=50),
        ),
    ]