from django.urls import path
from . import views


app_name = 'Team'
urlpatterns = [
 path('', (views.TeamAllView.as_view()), name='Overview'),
 path('<int:pk>/', (views.TeamDetailsView.as_view()), name='Details'),
 path('Create/', (views.TeamCreateView.as_view()), name='Create'),
 path("GenerateStage/<int:pk>/", views.GenerateStageGames.as_view(), name="Stage"),
 path("EditGame/<int:pk>/", views.GameChange.as_view(), name="Game"),
]
