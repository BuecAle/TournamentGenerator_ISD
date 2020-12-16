from django.urls import path
from . import views


app_name = 'Team'
urlpatterns = [
 path('', (views.TeamAllView.as_view()), name='Overview'),
 #example: --> http://127.0.0.1:8000/Team/
 path('<int:pk>/', (views.TeamDetailsView.as_view()), name='Details'),
 path('Create/', (views.TeamCreateView.as_view()), name='Create'),
 path("Stage/<int:pk>/<int:stage>/", views.ListStageGamesView.as_view(), name="Stage"),
 path("EditGame/<int:pk>/", views.GameChange.as_view(), name="Game"),
 #http://127.0.0.1:8000/Team/Create/ --> example: http://127.0.0.1:8000/Team/58/
]
