import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Person
from .forms import NameForm

# Create your views here.
def index(request):
    return render(request, "index.html")


def add_person(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_person = Person(
                first_name=form.data['first_name'],
                middle_names=form.data['middle_names'],
                last_name=form.data['last_name'],
                born=form.data['born'],
                died=form.data['died'] or None,
                father=form.data.get('father') or None,
                mother=form.data.get('mother') or None
            )
            new_person.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    else:
        form = NameForm()

    return render(request, 'new_person.html', {'form': form})


def db(request):

    persons = Person.objects.all()

    return render(request, "db.html", {"persons": persons})
