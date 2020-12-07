from django.urls import path
from . import views


app_name = 'Team'
urlpatterns = [
 path('', (views.TeamAllView.as_view()), name='Overview'),
 path('<int:pk>/', (views.TeamDetailsView.as_view()), name='Details'),
 path('Create/', (views.TeamCreateView.as_view()), name='Create'),
]
