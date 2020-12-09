from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Tournament.models import Tournament


# Create your models here.
class Team(models.Model):
    TeamName = models.CharField(max_length=120)
    NrOfPlayer = models.DecimalField(default=6, decimal_places=0, max_digits=2, validators=[MinValueValidator(5), MaxValueValidator(30)])
    Manager = models.CharField(max_length=120, default="")
    Captain = models.CharField(max_length=120, default="")
    Tournament = models.ForeignKey(Tournament, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.TeamName


class Game(models.Model):
    STAGE_CHOICES = (
        (16, "1 of 32"),
        (8, "1 of 16"),
        (4, "1 of 8"),
        (2, "1 of 4"),
        (1, "1 of 2")
    )
    team_a = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE, related_name="team_a")
    team_b = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE, related_name="team_b")
    team_a_points = models.IntegerField(default=0)
    team_b_points = models.IntegerField(default=0)
    played = models.BooleanField(default=False)
    stage = models.IntegerField(choices=STAGE_CHOICES, default=4, max_length=50)
    tournament = models.ForeignKey(Tournament, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_a.TeamName} vs {self.team_b.TeamName}"

