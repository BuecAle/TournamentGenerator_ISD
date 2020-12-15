from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Tournament.models import Tournament


# Create your models here.

# Team model: Teamname, Number of Player, Manager, Captain and Tournament
class Team(models.Model):
    TeamName = models.CharField(max_length=120)
    NrOfPlayer = models.DecimalField(default=6, decimal_places=0, max_digits=2, validators=[MinValueValidator(5), MaxValueValidator(30)])
    Manager = models.CharField(max_length=120, default="")
    Captain = models.CharField(max_length=120, default="")
    Tournament = models.ForeignKey(Tournament, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.TeamName
