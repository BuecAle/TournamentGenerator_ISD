from django.urls import path
from . import views
from Team.views import TeamCreateForTournamentView


app_name = 'Tournament'
urlpatterns = [
 path('', (views.TournamentAllView.as_view()), name='Overview'),
 path('<int:pk>/', (views.TournamentDetailsView.as_view()), name='Details'),
 path('Create/', (views.TournamentCreateView.as_view()), name='Create'),
 path('<int:pk>/CreateTeam/', (TeamCreateForTournamentView.as_view()), name='CreateTeamForTournament'),
 path('<int:pk>/Tree/', (views.TournamentTreeView.as_view()), name='Tree'),
]
