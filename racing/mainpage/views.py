from django.shortcuts import render

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
def team_profile(request, username):
    return render(
        request,     #так будет всегда(первым параметром будет request)
        'mainpage/news.html',
        context={
            "teamTitle": username, 
            "myphoto": "/static/logo/" + username + ".jfif"
        }
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