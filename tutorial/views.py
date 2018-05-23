from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable
from testpage.models import Urls
from runapp.models import Isue
from .tables import UrlsTable
from .tables import IsueTable
from runapp.mainapp.starter import startfirst
from runapp.mainapp.compliter import complete
from runapp.add_isue_attribute.search_keys import add_keys_img
from runapp.mainapp.finisher import finish

def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})

def myurl(request):
    table = UrlsTable(Urls.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})

def load(request):
    startfirst()
    table = IsueTable(Isue.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})

def getcotent(request):
    complete()
    table = IsueTable(Isue.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})

def reloadkey(request):
    add_keys_img()
    table = IsueTable(Isue.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})

def closeisues(request):
    finish()
    table = IsueTable(Isue.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})
