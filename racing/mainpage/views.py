from django.shortcuts import render

def index(request):
    context={
        'participants':[
            {'name':'RedBull'},
            {'name':'Mclaren'}

        ]
    }
    return render(
        request,     #так будет всегда(первым параметром будет request)
        'mainpage/index.html',
        context
    )
