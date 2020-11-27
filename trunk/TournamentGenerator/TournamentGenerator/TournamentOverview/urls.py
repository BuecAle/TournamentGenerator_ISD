"""studentSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.TournamentView.as_view(), name="tournament"),
    path("team_view/<int:pk>/", views.TeamView.as_view(), name="team_view"),
    path('create_tournament/', views.TournamentCreateView.as_view(), name="create_tournament"),
    path("create_team/<int:pk>/", views.TeamsCreateView.as_view(), name="create_team"),
    path("tournaments_list/", views.AllTournamentsView.as_view(), name="tournaments_list"),
    path("teams_list/<int:pk>/", views.TournamentTeamsView.as_view(), name="teams_list")
]
