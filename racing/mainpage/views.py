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
