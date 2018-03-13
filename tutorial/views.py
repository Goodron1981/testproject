from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable
from testpage.models import Urls
from testpage.models import Accounts
from .tables import UrlsTable
from .tables import AccountsTable
#from runapp.sape.autorization import autorizen
from runapp.sape.load_isue import load_isue

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
    load_isue()
    table = AccountsTable(Accounts.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})
