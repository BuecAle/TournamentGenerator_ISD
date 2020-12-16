from django.contrib import admin

from .models import Team


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team Details', {'fields': ['TeamName']}),
        (None, {'fields': ['NrOfPlayer']}),
        (None, {'fields': ['Manager']}),
        (None, {'fields': ['Captain']}),
        ('Tournament', {'fields': ['Tournament']}),
    ]
    # Shows Tournamentname and -Size
    list_display = ('TeamName', 'Tournament')
    # Filter where Teams can be filtered by Tournament
    list_filter = ['Tournament']
    # Field where Teams can be searched with Teamname
    search_fields = ['TeamName']


# Show Model Tournament on admin page
admin.site.register(Team, TeamAdmin)
