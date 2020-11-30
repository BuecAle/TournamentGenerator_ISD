from django.db import models
from django.urls import reverse
from django.shortcuts import redirect

# Create your models here.

class Tournament(models.Model):
    TOURNAMENT_CHOICES = (
        ('8teams', '8 Teams'),
        ('16teams', '16 Teams'),
        ('32teams', '32 Teams'),
    )
    TournamentName = models.CharField(max_length=120)
    TournamentSize = models.CharField(max_length=120, choices=TOURNAMENT_CHOICES, default='Tournamentsize')

    def get_absolute_url(self):
        return reverse("teams_list", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.TournamentName} with {self.TournamentSize} teams"


class Teams(models.Model):
    TeamName = models.CharField(max_length=120)
    NrOfPlayer = models.DecimalField(decimal_places=0, max_digits=2)
    Manager = models.CharField(max_length=120, default="")
    Captain = models.CharField(max_length=120, default="")
    tournament = models.ForeignKey(Tournament, blank=True, null=True, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse("team-view", kwargs={"pk" : self.tournament.id})

    def __str__(self):
        return f"{self.TeamName}"





