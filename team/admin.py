from django.contrib import admin

from team.models import Team, TeamMember


class TeamMemberInline(admin.StackedInline):
    model = TeamMember


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created_by",
        "description",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "name",
        "created_at",
        "updated_at",
    ]
    list_search = [
        "name",
        "created_at",
        "updated_at",
    ]
    inlines = [TeamMemberInline]


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "team",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "team",
        "created_at",
        "updated_at",
    ]
    list_search = [
        "team",
        "created_at",
        "updated_at",
    ]
