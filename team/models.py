from django.db import models
import auto_prefetch
from utils.models import NamedTimeBasedModel, TimeBasedModel

# Create your models here.
class Team(NamedTimeBasedModel):
    created_by = auto_prefetch.ForeignKey(
        "accounts.CustomUser",
        related_name="created_teams",
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=50)


class TeamMember(TimeBasedModel):
    user = auto_prefetch.ForeignKey(
        "accounts.CustomUser",
        related_name="member_teams",
        on_delete=models.CASCADE,
    )
    team = auto_prefetch.ForeignKey(
        "team.Team",
        related_name="team_members",
        on_delete=models.CASCADE,
    )
