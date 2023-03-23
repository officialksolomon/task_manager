from django.contrib import admin

# Register your models here.

from task.models import (
    Task,   
    TaskBoard,
    TaskCategory,
    TaskComment,
    TaskPriority,
)


class TaskCommentInline(admin.StackedInline):
    model = TaskComment


class TaskInline(admin.StackedInline):
    model = Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "board",
        "priority",
        "status",
        "assigned_to",
        "category",
        "due_date",
        "created_by",
    ]

    list_filter = [
        "priority",
        "status",
        "category",
        "due_date",
        "created_by",
    ]
    list_search = [
        "name",
        "description",
        "priority",
        "status",
        "category",
    ]

    ordering = ["status"]

    ordering = ["status"]


@admin.register(TaskBoard)
class TaskBoardAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "created_by",
    ]

    list_filter = [
        "name",
        "description",
    ]

    list_search = [
        "name",
        "description",
    ]

    ordering = ["created_at"]
    inlines = [TaskInline]


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]

    list_filter = [
        "name",
    ]

    list_search = [
        "name",
    ]

    ordering = ["created_at"]


@admin.register(TaskPriority)
class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        'level'
    
    ]

    list_filter = [
        "name",
       "level"
    ]

    list_search = [
        "name",
  
    ]

    ordering = ["created_at"]

