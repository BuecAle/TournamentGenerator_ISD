from django.contrib import admin

from .models import Tournament
from Team.models import Team


# Register your models here.
class TeamsInLine(admin.TabularInline):
    model = Team
    extra = 8


class TournamentAdmin(admin.ModelAdmin):
    fieldsets = [

    ]
    inlines = [TeamsInLine]
    list_display = ('TournamentName', 'TournamentSize')
    search_fields = ['TournamentName']


admin.site.register(Tournament, TournamentAdmin)
