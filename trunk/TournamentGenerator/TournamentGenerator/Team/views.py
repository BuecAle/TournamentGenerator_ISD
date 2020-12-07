from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View, generic

from Tournament.models import Tournament
from .models import Team, Game
from .forms import TeamCreateForm
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
        tournament: Tournament = Tournament.objects.get_object_or_404(pk=kwargs.get("pk"))

        teams = Team.objects.filter(Tournament=tournament.id)
        num_games = kwargs.get("stage")
        teams = [team for team in teams]
        while num_games > 0:
            team_a = random.choice(teams)
            teams = teams.remove(team_a)
            team_b = random.choice(teams)
            teams = teams.remove(team_b)
            Game.objects.create(
                team_a=team_a,
                team_b=team_b,
            )

        return redirect(reverse())


class ListStageGames(View):
    def get(self, request, *args, **kwargs):
        tournament = kwargs.get("pk")
