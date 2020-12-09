from django.shortcuts import render, redirect
from django.db.models import Count
from django.urls import reverse
from django.views import View, generic

from Tournament.models import Tournament
from .models import Team, Game
from .forms import TeamCreateForm, GameEditForm
import random


# Create your views here.
class TeamAllView(generic.ListView):
    template_name = 'Team/TeamOverview.html'

    def get_queryset(self):
        return Team.objects.all().order_by('TeamName')


class TeamDetailsView(View):
    def get(self, request, *args, **kwargs):
        team = Team.objects.get(pk=kwargs["pk"])
        opponents = Team.objects.filter(Tournament=team.Tournament).exclude(TeamName=team.TeamName)
        return render(request, "Team/TeamDetails.html", context={
            "pk": kwargs["pk"],
            "team": team,
            "opponents": opponents
        })


class TeamCreateView(View):
    def get(self, request):
        form = TeamCreateForm
        return render(request, "Team/TeamCreate.html", context={"form": form})

    def post(self, request):
        form = TeamCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("Team:Overview"))
        else:
            return redirect(reverse("Team:Create"))


class TeamCreateForTournamentView(View):
    def get(self, request, *args, **kwargs):
        tournament = Tournament.objects.get(pk=kwargs["pk"])
        form = TeamCreateForm(initial={'Tournament': tournament})
        remainingTeams = int(tournament.TournamentSize[0]) - Team.objects.filter(Tournament=tournament).count()
        if remainingTeams == 0:
            tournament_complete = True
        else:
            tournament_complete = False
        return render(request, "Tournament/TournamentCreateTeam.html", context={
            "form": form,
            "tournament": tournament,
            "remainingTeams": remainingTeams,
            "tournament_complete": tournament_complete
        })

    def post(self, request, *args, **kwargs):
        form = TeamCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            tournament = Tournament.objects.get(pk=kwargs["pk"])
            form.instance.tournament = tournament
            teams_remain = int(tournament.TournamentSize[0])- Team.objects.filter(Tournament=tournament).count()
            if teams_remain > 0:
                form.save()
                return redirect(reverse("Tournament:Details", kwargs={"pk": kwargs["pk"]}))
            else:
                form.clean()
                return redirect(reverse("Tournament:CreateTeamForTournament", kwargs={"pk": kwargs["pk"]}))
        else:
            return redirect(reverse("Tournament:Details", kwargs={"pk": kwargs["pk"]}))


class GenerateStageGames(View):
    def get(self, request, *args, **kwargs):
        tournament: Tournament = Tournament.objects.get(pk=kwargs.get("pk"))

        stage = tournament.get_stage()
        games = tournament.game_set.filter(stage=stage*2)
        if games.count() == 0 or games.filter(
                played=True).aggregate(Count("played"))["played__count"] == stage*2:
            games = tournament.generate_stage()

        return render(request, "Team/Stage.html", context={
            "games": games, "pk":tournament.id,
        })


class GameChange(generic.UpdateView):
    template_name = "Team/GameChange.html"
    form_class = GameEditForm
    model = Game


class ListStageGames(View):
    def get(self, request, *args, **kwargs):
        tournament = kwargs.get("pk")
