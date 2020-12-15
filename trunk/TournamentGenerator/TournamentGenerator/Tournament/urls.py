from django.urls import path
from . import views
from Team.views import TeamCreateForTournamentView


app_name = 'Tournament'
urlpatterns = [
 path('', (views.TournamentAllView.as_view()), name='Overview'),
 #example: --> http://127.0.0.1:8000/Tournament/
 path('<int:pk>/', (views.TournamentDetailsView.as_view()), name='Details'),
 path('Create/', (views.TournamentCreateView.as_view()), name='Create'),
 #example: --> http://127.0.0.1:8000/Tournament/Create/
 path('<int:pk>/CreateTeam/', (TeamCreateForTournamentView.as_view()), name='CreateTeamForTournament'),
 #example: --> http://127.0.0.1:8000/Team/Create/
 path('<int:pk>/Tree/', (views.TournamentTreeView.as_view()), name='Tree'),
 #example: --> http://127.0.0.1:8000/Tournament/16/Tree/
]
