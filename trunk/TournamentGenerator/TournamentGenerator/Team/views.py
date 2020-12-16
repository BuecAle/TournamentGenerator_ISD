from django.shortcuts import render, redirect
from django.db.models import Count
from django.urls import reverse
from django.views import View, generic
from django.utils.crypto import get_random_string

from Tournament.models import Tournament
from .models import Team, Game
from .forms import TeamCreateForm, GameEditForm
import random


# Create your views here.

# A List view where all created Teams are listed
class TeamAllView(generic.ListView):
    template_name = 'Team/TeamOverview.html'

    def get_queryset(self):
        return Team.objects.all().order_by('TeamName')


# Detailview of the Team:
#   - Shows the Teamname, Number of Player, Manager, Captain and the Tournament
#   - Shows all the games of the Team
class TeamDetailsView(View):
    def get(self, request, *args, **kwargs):
        team = Team.objects.get(pk=kwargs["pk"])
        opponents = Team.objects.filter(Tournament=team.Tournament).exclude(TeamName=team.TeamName)
        return render(request, "Team/TeamDetails.html", context={
            "pk": kwargs["pk"],
            "team": team,
            "opponents": opponents
        })


# Empty File to create a new Team
#   - Can be created for Tournament or just the Team
class TeamCreateView(View):
    def get(self, request):
        form = TeamCreateForm
        return render(request, "Team/TeamCreate.html", context={"form": form})

    def post(self, request):
        form = TeamCreateForm(request.POST)
        # If: Input is valid: Back to all Teams
        if form.is_valid():
            form.save()
            return redirect(reverse("Team:Overview"))
        # Else: Reload empty creation file
        else:
            return redirect(reverse("Team:Create"))


# Empty File to create a new Team for the specific Tournament
#   - Tournament is already filled in
class TeamCreateForTournamentView(View):
    def get(self, request, *args, **kwargs):
        tournament = Tournament.objects.get(pk=kwargs["pk"])
        tournamentsize = Tournament.get_TournamentSize(tournament)
        form = TeamCreateForm(initial={'Tournament': tournament})
        remainingTeams = int(tournament.TournamentSize.split()[0]) - Team.objects.filter(Tournament=tournament).count()
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
            tournamentsize = Tournament.get_TournamentSize(tournament)
            form.instance.tournament = tournament
            teams_remain = int(tournament.TournamentSize.split()[0])- Team.objects.filter(Tournament=tournament).count()
            if teams_remain > 0:
                form.save()
                return redirect(reverse("Tournament:Details", kwargs={"pk": kwargs["pk"]}))
            else:
                form.clean()
                return redirect(reverse("Tournament:CreateTeamForTournament", kwargs={"pk": kwargs["pk"]}))
        else:
            return redirect(reverse("Tournament:Details", kwargs={"pk": kwargs["pk"],"errors": form.errors}))


class ListStageGamesView(View):
    def get(self, request, *args, **kwargs):
        tournament: Tournament = Tournament.objects.get(pk=kwargs.get("pk"))
        stage = kwargs.get("stage")
        games = Game.objects.filter(tournament=tournament, stage=stage)

        return render(request, "Team/Stage.html", context={
            "games": games, "pk":tournament.id,
        })


class GameChange(View):
    def get(self, request, *args, **kwargs):
        game = Game.objects.get(id=kwargs.get("pk"))
        form = GameEditForm

        return render(request, "Team/GameChange.html", context={
            "form": form, "pk":game.id, "game":game,
        })

    def post(self, request, *args, **kwargs):
        game = Game.objects.get(id=kwargs.get("pk"))
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
        return redirect(reverse("Team:Stage", kwargs={"pk": form.instance.tournament.id, "stage":game.stage}))


class ListStageGames(View):
    def get(self, request, *args, **kwargs):
        tournament = kwargs.get("pk")

            return redirect(reverse("Tournament:Details", kwargs={"pk": kwargs["pk"]}))


# Create new Team for specific Tournament
#   - All fields are already field with random Strings
class TeamAutoCreateView(View):
    def get(self, request, *args, **kwargs):
        tournament = Tournament.objects.get(pk=kwargs["pk"])
        tournamentsize = Tournament.get_TournamentSize(tournament)
        teamname = get_random_string(length=10, allowed_chars='Team')
        manager = get_random_string(length=7, allowed_chars='Manager')
        captain = get_random_string(length=7, allowed_chars='Captain')
        form = TeamCreateForm(initial={'TeamName': teamname,
                                       'Manager': manager,
                                       'Captain': captain,
                                       'Tournament': tournament,
                                       })
        remainingTeams = tournamentsize - Team.objects.filter(Tournament=tournament).count()
        # To show the number of Teams which have to be created for the Tournament
        if remainingTeams == 0:
            tournament_complete = True
        else:
            tournament_complete = False
        return render(request, "Tournament/TournamentAutoCreate.html", context={
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
            tournamentsize = Tournament.get_TournamentSize(tournament)
            form.instance.tournament = tournament
            teams_remain = tournamentsize - Team.objects.filter(
                Tournament=tournament).count()
            # To show the number of Teams which have to be created for the Tournament
            if teams_remain > 0:
                form.save()
                return redirect(reverse("Tournament:AutoCreate", kwargs={"pk": kwargs["pk"]}))
            else:
                form.clean()
                return redirect(reverse("Tournament:AutoCreate", kwargs={"pk": kwargs["pk"]}))
        else:
            return redirect(reverse("Tournament:Details", kwargs={"pk": kwargs["pk"]}))