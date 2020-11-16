from django.contrib import admin

from .models import Teams, Tournament

# Register your models here.
admin.site.register(Teams)
admin.site.register(Tournament)