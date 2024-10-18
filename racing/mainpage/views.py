from django.shortcuts import render
import os

def index(request):
    context={
        'participants':[
            {'name':'RedBull'},
            {'name':'Mclaren'},
            {'name':'Ferrari'},
            {'name':'Mercedes'},
            {'name':'AstonMartin'},
            {'name':'RacingBulls'},
            {'name':'Haas'},
            {'name':'Alpine'},
            {'name':'Williams'},
            {'name':'KickSauber'}

        ]
    }
    return render(
        request,     #так будет всегда(первым параметром будет request)
        'mainpage/index.html',
        context
    )
def team_profile(request, team_name):
    team_path = 'mainpage/templates/mainpage/%s' % team_name
    if not os.path.exists(team_path):
        return render(
            request,     #так будет всегда(первым параметром будет request)
            'mainpage/news.html',
            context={
                "teamTitle": team_name, 
                "myphoto": "/static/logo/" + team_name + ".jfif",
                'tm': team_name,
                'articles': []
            }
        )
    print(os.listdir())
    return render(
        request,     #так будет всегда(первым параметром будет request)
        'mainpage/news.html',
        context={
            "teamTitle": team_name, 
            "myphoto": "/static/logo/" + team_name + ".jfif",
            'tm': team_name,
            'articles': os.listdir('mainpage/templates/mainpage/%s' % team_name)
        }
    )

def article(request, team_name, artid):
    return render(
        request,     #так будет всегда(первым параметром будет request)
        'mainpage/%s/%s' % (team_name, artid),
    )


 
from django.http import HttpResponse 
def get_content(request, contenti): 
    import os 
    print(os.getcwd()) 
    content = open( 
        'mainpage/static/posts/p%i.html' % contenti, 
        encoding='utf-8').read() 
    print(content) 
    return HttpResponse(content)

from . import models

def positions(request): #, username):
    pilots = models.Pilot.objects.all()
    return render(
        request,     #так будет всегда(первым параметром будет request)
        'mainpage/drivers.html',
        context={
            'pilots': pilots
        }
    )


def positions(request): #, username):
    pilots = models.Pilot.objects.all()
    return render(
        request,     #так будет всегда(первым параметром будет request)
        'mainpage/drivers.html',
        context={
            'pilots': pilots
        }
    )