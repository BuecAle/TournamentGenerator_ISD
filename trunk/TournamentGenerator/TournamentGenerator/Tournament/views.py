from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View, generic
from django.db.models import Min

from .forms import TournamentCreateForm
from .models import Tournament
from Team.models import Team, Game


# Create your views here.
class TournamentAllView(generic.ListView):
    template_name = 'Tournament/TournamentOverview.html'

    def get_queryset(self):
        return Tournament.objects.all().order_by('TournamentName')


class TournamentDetailsView(View):
   def get(self, request, *args, **kwargs):
       tournament = Tournament.objects.get(pk=kwargs["pk"])
       team = Team.objects.filter(Tournament=kwargs["pk"])
       remainingTeams = int(tournament.TournamentSize.split()[0]) - Team.objects.filter(Tournament=tournament).count()
       stages = []
       if remainingTeams == 0:
           stage = tournament.get_stage()
           if tournament.game_set.all().aggregate(Min("stage"))["stage__min"] != stage:
               tournament.generate_stage()
           stages = tournament.game_set.all().order_by("-stage").values_list("stage", flat=True).distinct()
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
           "stages": stages,
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



