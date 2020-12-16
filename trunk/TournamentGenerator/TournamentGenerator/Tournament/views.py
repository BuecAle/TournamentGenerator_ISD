from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View, generic

from .forms import TournamentCreateForm
from .models import Tournament
from Team.models import Team


# Create your views here.

# A List view where all created Tournaments are listed
class TournamentAllView(generic.ListView):
    template_name = 'Tournament/TournamentOverview.html'

    def get_queryset(self):
        return Tournament.objects.all().order_by('TournamentName')


# Detailview of the Tournament:
#   - Shows the Tournamentname, Number of Teams
#   - Shows all the Teams of the Tournament
class TournamentDetailsView(View):
    def get(self, request, **kwargs):
        tournament = Tournament.objects.get(pk=kwargs["pk"])
        tournamentsize = Tournament.get_TournamentSize(tournament)
        team = Team.objects.filter(Tournament=tournament)
        remainingteams = tournamentsize - Team.objects.filter(Tournament=tournament).count()
        # To show the number of Teams which have to be created for the Tournament
        if remainingteams == 0:
            tournament_complete = True
        else:
            tournament_complete = False
        return render(request, "Tournament/TournamentDetails.html", context={
           "pk": kwargs["pk"],
           "tournament": tournament,
           "team": team,
           "remainingteams": remainingteams,
           "tournament_complete": tournament_complete,
        })


# Empty File to create a new Tournament
class TournamentCreateView(View):
    def get(self, request):
        form = TournamentCreateForm
        return render(request, "Tournament/TournamentCreate.html", context={"form": form})

    def post(self, request):
        form = TournamentCreateForm(request.POST)
        # If: Input is valid: Back to the Details of the Tournament
        if form.is_valid():
            form.save()
            return redirect(reverse("Tournament:Details", kwargs={"pk": form.instance.id}))
        # Else: Reload empty creation file
        return redirect(reverse("Tournament:Overview"))


# Shows a generated Tournament Tree
class TournamentTreeView(View):
    def get(self, request, **kwargs):
        tournament = Tournament.objects.get(pk=kwargs["pk"])
        tournamentsize = Tournament.get_TournamentSize(tournament)
        team = Team.objects.filter(Tournament=tournament)
        firstteams = team[:(tournamentsize/2)]
        secondteams = team[(tournamentsize/2):]
        remainingteams = tournamentsize - team.count()
        # To show the number of Teams which have to be created for the Tournament
        if remainingteams == 0:
            tournament_complete = True
        else:
            tournament_complete = False
        return render(request, "Tournament/TournamentTree.html", context={
           "pk": kwargs["pk"],
           "tournament": tournament,
           "tournamentsize": tournamentsize,
           "team": team,
           "firstteams": firstteams,
           "secondteams": secondteams,
           "remainingteams": remainingteams,
           "tournament_complete": tournament_complete,
        })
