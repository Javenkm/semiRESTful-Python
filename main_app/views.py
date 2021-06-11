from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Shows

def update(request, id):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/edit/'+id)
    else:
        shows = Shows.objects.get(id = id)
        shows.title = request.POST['title']
        shows.description = request.POST['description']
        shows.save()
        messages.success(request, "Show successfully updated")
        return redirect('/shows')
# Create your views here.

def index(request):
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, 'index.html', context)


# def shows(request):



def new(request):
    Show.objects.create (
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return render (request, 'tvShows.html')