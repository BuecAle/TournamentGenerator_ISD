from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View, generic

from .forms import TournamentCreateForm
from .models import Tournament
from Team.models import Team


# Create your views here.
class TournamentAllView(generic.ListView):
    template_name = 'Tournament/TournamentOverview.html'

    def get_queryset(self):
        return Tournament.objects.all().order_by('TournamentName')


class TournamentDetailsView(View):
   def get(self, request, *args, **kwargs):
       tournament = Tournament.objects.get(pk=kwargs["pk"])
       tournamentsize = Tournament.get_TournamentSize(tournament)
       team = Team.objects.filter(Tournament=tournament)
       remainingTeams = tournamentsize - Team.objects.filter(Tournament=tournament).count()
       if remainingTeams == 0:
           tournament_complete = True
       else:
           tournament_complete = False
       return render(request, "Tournament/TournamentDetails.html", context={
           "pk": kwargs["pk"],
           "tournament": tournament,
           "team": team,
           "remainingTeams": remainingTeams,
           "tournament_complete": tournament_complete,
       })


class TournamentCreateView(View):
    def get(self, request):
        form = TournamentCreateForm
        return render(request, "Tournament/TournamentCreate.html", context={"form": form})

    def post(self, request):
        form = TournamentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("Tournament:Details", kwargs={"pk": form.instance.id}))

        return redirect(reverse("Tournament:Overview"))


class TournamentTreeView(View):
   def get(self, request, *args, **kwargs):
       tournament = Tournament.objects.get(pk=kwargs["pk"])
       tournamentsize = Tournament.get_TournamentSize(tournament)
       team = Team.objects.filter(Tournament=tournament)
       firstteams = team[:(tournamentsize/2)]
       secondteams = team[(tournamentsize/2):]
       remainingTeams = tournamentsize - team.count()
       if remainingTeams == 0:
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
           "remainingTeams": remainingTeams,
           "tournament_complete": tournament_complete,
       })

# class TournamentGames(View):
#     def get(self, request, *args, **kwargs):
#         tournament = Tournament.objects.get(pk=kwargs["pk"])
#         tournamentsize = Tournament.get_TournamentSize(tournament)
#         team = Team.objects.filter(Tournament=tournament)
#         firstteams = team[:(tournamentsize / 2)]
#         secondteams = team[(tournamentsize / 2):]
#         for i in firstteams:
#         for p in secondteams:
#             if i==p:
#                 winner
#         return render(request, "Tournament/TournamentRound.html", context={
#             "pk": kwargs["pk"],
#             "tournament": tournament,
#             "tournamentsize": tournamentsize,
#             "team": team,
#             "firstteams": firstteams,
#             "secondteams": secondteams,
#             "remainingTeams": remainingTeams,
#             "tournament_complete": tournament_complete,
#         })



