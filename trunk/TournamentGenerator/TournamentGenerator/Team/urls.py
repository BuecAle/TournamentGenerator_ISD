from django.urls import path
from . import views


app_name = 'Team'
urlpatterns = [
 path('', (views.TeamAllView.as_view()), name='Overview'),
 # example: --> http://127.0.0.1:8000/Team/
 path('<int:pk>/', (views.TeamDetailsView.as_view()), name='Details'),
 # example: --> http://127.0.0.1:8000/Team/16
 path('Create/', (views.TeamCreateView.as_view()), name='Create'),
 # http://127.0.0.1:8000/Team/Create/
]
