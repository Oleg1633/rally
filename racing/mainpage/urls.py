from django.urls import path
from . import views

urlpatterns = [
    path('',                            views.index,        name='mainpage'),
    path('positions/',                  views.positions,    name='positions'),
    path('aboutUs/',                    views.aboutUs,      name='about'),
    path('<str:team_name>/',            views.team_profile, name='team_profile'),
    path('<str:team_name>/<str:artid>', views.article,      name='article'),
    path('content/<int:contenti>/',     views.get_content,  name='get_content'),
    path('login/',                      views.login,        name='log'),
    path('callback/',                   views.callback,     name='call'),
    
]