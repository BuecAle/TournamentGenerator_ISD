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
    path('', TemplateView.as_view(template_name="GettingStarted.html"), name='GettingStarted'),
    path('Tournament/', include('Tournament.urls')),
    path('Team/', include('Team.urls')),
    path('About/', TemplateView.as_view(template_name="About.html"), name='About'),
    path('Imprint/', TemplateView.as_view(template_name="Imprint.html"), name='Imprint')
    # path('home/', tournamentCreateView),
    # path('teams/', teamList),
    # path('', tournamentCreateView),
    # path('team/', include('TournamentOverview.urls')),
    # path('tournamenttree/', teamOne),
]
