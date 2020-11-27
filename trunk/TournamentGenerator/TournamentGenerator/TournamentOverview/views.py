from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from django.views import View

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


# def teamList(httprequest, *args, **kwargs):
#     allTeams = Teams.objects.all()
#     context ={
#         "allTeams" : allTeams,
#         "title" : "My team list"
#     }
#
#     return render(httprequest, "team_list.html", context)
#
#
#
# def teamDetail(httprequest, my_id, *args, **kwargs):
#     oneTeam =get_object_or_404(Teams, id=my_id)
#     context ={
#         "obj" : oneTeam,
#         "title" : "Team Details"
#     }
#
#     return render(httprequest, "team_detail.html", context)
#
#
# def teamOne(request):
#     all_teams = Teams.objects.all()
#
#     context = {
#         "all_teams": all_teams,
#         "TeamA": all_teams[0],
#         "TeamB": all_teams[1],
#         "TeamC": all_teams[2],
#         "TeamD": all_teams[3],
#         "TeamE": all_teams[4],
#         "TeamF": all_teams[5],
#         "TeamG": all_teams[6],
#         "TeamH": all_teams[7],
#     }
#
#     return render(request, "tournament_tree.html", context)


class TournamentView(View):
    def get(self, request, *args, **kwargs):
        form = TournamentCreateForm
        return render(request, "home.html", context={"form": form})


class TournamentCreateView(View):

    def post(self, request, *args, **kwargs):
        form = TournamentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("team_view", kwargs={"pk": form.instance.id}))

        return redirect(reverse("tournament"))


class TeamView(View):

    def get(self, request, *args, **kwargs):
        form = TeamCreateForm
        tournament = Tournament.objects.get(pk=kwargs["pk"])
        teams_remain = int(tournament.TournamentSize[0]) - Teams.objects.filter(tournament=tournament).count()
        return render(
            request, "team_create_view.html",
            context={
                "form": form,
                "pk": kwargs["pk"],
                "teams_remain": teams_remain,
            })


class TeamsCreateView(View):

    def post(self, request, *args, **kwargs):
        form = TeamCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            tournament = Tournament.objects.get(pk=kwargs["pk"])
            form.instance.tournament = tournament
            form.save()
            teams_remain = int(tournament.TournamentSize[0]) - Teams.objects.filter(tournament=tournament).count()
            if teams_remain > 0:
                return redirect(reverse("team_view", kwargs={"pk": kwargs["pk"]}))
            else:
                return redirect(tournament.get_absolute_url())
        else:
            return redirect(reverse("team_view", kwargs={"pk": kwargs["pk"]}))


class TournamentTeamsView(View):

   def get(self, request, *args, **kwargs):
       tournament = Tournament.objects.get(pk=kwargs["pk"])
       teams = Teams.objects.filter(tournament=tournament)
       return render(request, "team_list.html", context={"Teams": teams})


class AllTournamentsView(View):
    def get(self, request, *args, **kwargs):
        tournaments = Tournament.objects.all()
        return render(request, "tournaments_list.html", context={"Tournaments": tournaments})