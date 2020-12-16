from django.db import models
from django.apps import apps
from django.urls import reverse
import random

# Create your models here.

# Tournament model with Tournamentname and Tournamentsize(3 choices)
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

    def get_stage(self):
        min_stage = self.game_set.all().aggregate(models.Min("stage"))["stage__min"]
        num_of_games = self.game_set.filter(stage=min_stage).count()
        if self.game_set.all().count() == 0:
            return int(self.TournamentSize.split()[0])//2
        elif self.game_set.filter(played=True, stage=min_stage).count() == num_of_games:
            return min_stage // 2
        else:
            return min_stage

    def create_stage(self, stage, teams):
        i = stage
        Game = apps.get_model("Team", "Game")
        while i > 0:
            team_a = random.choice(teams)
            teams = teams.exclude(id=team_a.id)
            team_b = random.choice(teams)
            teams = teams.exclude(id=team_b.id)
            game = Game.objects.create(
                team_a=team_a,
                team_b=team_b,
                tournament=self,
                stage=stage
            )
            i -= 1

    def generate_stage(self):
        stage = self.get_stage()
        if stage == int(self.TournamentSize.split()[0])//2:
            teams = self.team_set.all()
            self.create_stage(stage, teams)
        else:
            games = self.game_set.filter(stage=stage*2)
            teams = []
            for game in games:
                if game.team_a_points > game.team_b_points:
                    teams.append(game.team_a.id)
                else:
                    teams.append(game.team_b.id)
            teams = self.team_set.filter(id__in=teams)
            self.create_stage(stage, teams)

        return self.game_set.filter(stage=stage)



    # Returns Tournamentsize as number depending on the chosen Tournamentsize
    def get_TournamentSize(self):
        if self.TournamentSize == "8 Teams":
            tournamentsize = 8
        elif self.TournamentSize == "16 Teams":
            tournamentsize = 16
        elif self.TournamentSize == "32 Teams":
            tournamentsize = 32
        return tournamentsize
