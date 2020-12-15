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
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path for admin site
    path('', TemplateView.as_view(template_name="GettingStarted.html"), name='GettingStarted'),
    #Starting Page of Tournament Generator --> Homepage/Landingpage
    path('Tournament/', include('Tournament.urls')),
    #example: Tournament/16/; shows Tournamentdetails and information if all teams created
    path('Team/', include('Team.urls')),
    #example: teams/67/; general information and games
    path('Samples/', TemplateView.as_view(template_name="Samples.html"), name='Samples'),
    #path to Samples; blank tournamenttrees 8/16/32
    path('About/', TemplateView.as_view(template_name="About.html"), name='About'),
    #path Aboutsite, extends simple html base
    path('Imprint/', TemplateView.as_view(template_name="Imprint.html"), name='Imprint')
    #path to Imprint page, extends simple html base
    # path('home/', tournamentCreateView),
    # path('teams/', teamList),
    # path('', tournamentCreateView),
    # path('team/', include('TournamentOverview.urls')),
    # path('tournamenttree/', teamOne),
]
