from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('<str:username>/', views.team_profile, name='team_profile'),
]