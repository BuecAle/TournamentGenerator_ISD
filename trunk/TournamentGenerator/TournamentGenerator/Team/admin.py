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
    list_display = ('TeamName', 'Tournament')
    list_filter = ['Tournament']
    search_fields = ['TeamName']


admin.site.register(Team, TeamAdmin)
