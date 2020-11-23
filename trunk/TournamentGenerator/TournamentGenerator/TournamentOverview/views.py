from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView

from .forms import RawTeamForm, TeamCreateForm, TournamentCreateForm
from .models import Teams, Tournament

# Create your views here.


# def teamCreateView(request, *args):
#     my_form = TeamCreateForm(request.POST)
#     if my_form.is_valid():
#         my_form.save(commit=False)
#
#
#     context = {
#         "form": my_form
#     }
#
#     return render(request, "team_create_view.html", context)


def teamList(httprequest, *args, **kwargs):
    allTeams = Teams.objects.all()
    context ={
        "allTeams" : allTeams,
        "title" : "My team list"
    }

    return render(httprequest, "team_list.html", context)



def teamDetail(httprequest, my_id, *args, **kwargs):
    oneTeam =get_object_or_404(Teams, id=my_id)
    context ={
        "obj" : oneTeam,
        "title" : "Team Details"
    }

    return render(httprequest, "team_detail.html", context)


def teamOne(request):
    all_teams = Teams.objects.all()

    context = {
        "all_teams": all_teams,
        "TeamA": all_teams[0],
        "TeamB": all_teams[1],
        "TeamC": all_teams[2],
        "TeamD": all_teams[3],
        "TeamE": all_teams[4],
        "TeamF": all_teams[5],
        "TeamG": all_teams[6],
        "TeamH": all_teams[7],
    }

    return render(request, "tournament_tree.html", context)


class TournamentsView(ListView):
    model = Tournament
    queryset = Tournament.objects.all()
    template_name = "home.html"


class TournamentCreateView(View):

    def post(self, request):
        form = TournamentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("create_teams", kwargs={"pk": form.instance.id}))

        return redirect(reverse("create_tournament_view"))


class TeamsCreateView(View):
    template_name = "team_create_view.html"

    def post(self, request, pk):
        form = TeamCreateForm(request.POST)
        try:
            tournament = Tournament.objects.get(id=pk)
        except Tournament.DoesNotExists:
            return "Not such tournament"
        if form.is_valid():
            form.save(commit=False)
            form.tournament = tournament
            form.save()
            if Teams.objects.filter(tournament=tournament).count() != tournament.TournamentSize:
                return redirect("create_teams", kwargs={"pk": pk})
        return redirect("create_teams", kwargs={"pk": pk})


# def tournamentCreateView(request, *args, **kwargs):
#     my_form = TournamentCreateForm(request.POST)
#     context = {
#         "form": my_form
#     }
#     if my_form.is_valid():
#         my_form.save()
#         return redirect("teamCreateView", pk=my_form.instance.id)
#
#     return render(request, "home.html", context)