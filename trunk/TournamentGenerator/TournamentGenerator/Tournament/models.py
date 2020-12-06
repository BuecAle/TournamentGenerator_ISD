from django.db import models
from django.urls import reverse

from Team.models import Game


# Create your models here.
class Tournament(models.Model):
    TOURNAMENT_CHOICES = (
        ('8 Teams', '8 Teams'),
        ('16 Teams', '16 Teams'),
        ('32 Teams', '32 Teams'),
    )
    TournamentName = models.CharField(max_length=120)
    TournamentSize = models.CharField(max_length=120, choices=TOURNAMENT_CHOICES, default='Tournamentsize')

    def get_absolute_url(self):
        return reverse("Tournament:Details", kwargs={"pk": self.id})

    def __str__(self):
        return self.TournamentName


class Stage(models.Model):
    CHOOSE_STAGE = (
        (1, "Final"),

    )
    game = models.ForeignKey(Game, blank=True, null=True, on_delete=models.SET_NULL)
