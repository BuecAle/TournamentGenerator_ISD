from django.db import models
from django.urls import reverse

# Create your models here.


class Teams(models.Model):
    TeamName = models.CharField(max_length=120)
    NrOfPlayer = models.DecimalField(decimal_places=0, max_digits=2)
    Manager = models.CharField(max_length=120, default="")
    Captain = models.CharField(max_length=120, default="");

    def get_absolute_url(self):
        return reverse("team-detail", kwargs={"my_id" : self.id})



class Tournament(models.Model):
    TOURNAMENT_CHOICES = (
        ('8teams', '8 Teams'),
        ('16teams', '16 Teams'),
        ('32teams', '32 Teams'),
    )
    TournamentName = models.CharField(max_length=120)
    TournamentSize = models.CharField(max_length=120, choices=TOURNAMENT_CHOICES, default='Tournamentsize')

    def get_absolute_url(self):
        return reverse("team-detail", kwargs={"my_id" : self.id})

