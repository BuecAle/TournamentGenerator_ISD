from django.shortcuts import render, get_object_or_404

from .forms import RawTeamForm, TeamCreateForm
from .models import Teams

# Create your views here.


def teamCreateView(httprequest, *args, **kwargs):
    my_form = TeamCreateForm(httprequest.POST or None)

    if my_form.is_valid():
        my_form.save()        #Products.objects.create(**my_form.cleaned_data)
        my_form = TeamCreateForm()

    context = {
        "form": my_form
    }

    return render(httprequest, "team_create_view.html", context)

"""
def teamCreateView(httprequest, *args, **kwargs):
    my_form = RawProductForm(httprequest.POST or None)
    print(httprequest.POST)
    if my_form.is_valid():
        #print(**my_form.cleaned_data)
        Products.objects.create(**my_form.cleaned_data)
        my_form = RawProductForm()

    context ={
        "form" : my_form
    }

    return render(httprequest, "team_list.html", context)
"""


def teamList(httprequest, *args, **kwargs):
    allTeams = Teams.objects.all()
    context ={
        "allTeams" : allTeams,
        "title" : "My team list"
    }

    return render(httprequest, "team_list.html", context)

"""
def teamListTournamentTree(httprequest, *args, **kwargs):
    allTeams = Teams.objects.filter(TeamName="Team1")
    context ={
        "allTeams" : allTeams,
        "title" : "My teams"
    }

    return render(httprequest, "tournament_tree.html", context)
"""



def teamDetail(httprequest, my_id, *args, **kwargs):
    #oneProduct = Products.objects.get(id=my_id)
    oneTeam =get_object_or_404(Teams, id=my_id)
    context ={
        "obj" : oneTeam,
        "title" : "Team Details"
    }

    return render(httprequest, "team_detail.html", context)


def teamOne(request):
    all_teams = Teams.objects.all()
   # for i in all_teams:
    #        = all_teams[i]
    TeamA = all_teams[0]
    TeamB = all_teams[1]
    TeamC = all_teams[2]
    TeamD = all_teams[3]
    TeamE = all_teams[4]
    TeamF = all_teams[5]
    TeamG = all_teams[6]
    TeamH = all_teams[7]
    context = {
        "TeamA": TeamA,
        "TeamB": TeamB,
        "TeamC": TeamC,
        "TeamD": TeamD,
        "TeamE": TeamE,
        "TeamF": TeamF,
        "TeamG": TeamG,
        "TeamH": TeamH,
    }

    return render(request, "tournament_tree.html", context)


"""
def teamPlayer(httprequest, *args):
    my_dict = {
        "myList": ["this", "is", "my", "list", "hello"],
    }
    return render(httprequest, "home.html", my_dict)
"""