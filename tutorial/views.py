from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable
from testpage.models import Urls
from testpage.models import Accounts
from runapp.models import Isue
from .tables import UrlsTable
from .tables import AccountsTable
from .tables import IsueTable
from runapp.rota.load_isue import load_isue_rota
from runapp.sape.load_isue import load_isue_sape

def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})

def myurl(request):
    table = UrlsTable(Urls.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})

def myacaunts(request):
    #autorizen()
    load_isue_rota()
    #load_isue_sape()
    table = IsueTable(Isue.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})
