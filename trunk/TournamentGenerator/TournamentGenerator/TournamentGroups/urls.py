from django.urls import path

from . import views

urlpatterns =[
    path('Moedi/', views.home_view, name='home_view'),
    path('Johny/', views.HomeViewC, name='HomeViewC'),
]
