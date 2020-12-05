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
       team = Team.objects.filter(Tournament=kwargs["pk"])
       remainingTeams = int(tournament.TournamentSize[0]) - Team.objects.filter(Tournament=tournament).count()
       return render(request, "Tournament/TournamentDetails.html", context={
           "pk": kwargs["pk"],
           "tournament": tournament,
           "team": team,
           "remainingTeams": remainingTeams,
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



