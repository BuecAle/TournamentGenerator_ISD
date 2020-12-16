from django.contrib import admin

from .models import Tournament
from Team.models import Team


# Register your models here.
class TeamsInLine(admin.TabularInline):
    model = Team
    extra = 8


class TournamentAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [TeamsInLine]
    # Shows Tournamentname and -Size
    list_display = ('TournamentName', 'TournamentSize')
    # Field where Tournaments can be searched with Tournamentname
    search_fields = ['TournamentName']


# Show Model Tournament on admin page
admin.site.register(Tournament, TournamentAdmin)
