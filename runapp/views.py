import traceback

from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from testpage.models import Urls
from  django.http import HttpResponse
import time
from runapp.mainapp.starter import startfirst
from runapp.mainapp.finisher import finish
from runapp.mainapp.compliter import complete
from runapp.add_isue_attribute.search_keys import add_keys_img

# Create your views here.

def index(request):
    if request.method == 'POST':
        pk=request.POST['but']
        if pk == 'start':
            return render(request, 'runapp/index.html',{'shuffl':datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")})
        else:
            return render(request, 'runapp/index.html')
    else:
        return render(request, 'runapp/index.html')

def subpage(request):
    now = datetime.now()
    return render(request, 'runapp/index.html',{'shuffl':datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")})

def phone_filter(request):
    if request.method == 'GET':
        phone = request.GET.get('phone')
        queryset = Urls.objects.all()
        queryset = queryset.filter(url__contains=phone)
        #queryset = "Test"
        #phone = request.GET.get('phone')

            #queryset = queryset.filter(phone__contains=phone)
            #queryset = "Test"
        response = render(request,'runapp/phone-filter.html', {'phonenumbers':queryset})
        return response

def runner_filter(request):
    if request.method == 'GET':
        queryset = Urls.objects.all()
        #queryset = "Test"
        #phone = request.GET.get('phone')

            #queryset = queryset.filter(phone__contains=phone)
            #queryset = "Test"
        response = render(request,'runapp/phone-filter.html', {'phonenumbers':queryset})
        return response

def startpage(request):
    if request.method == 'POST':
        pk=request.POST['but']
        if pk == 'start':
            return render(request, 'runapp/startpage.html',{'shuffl':datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")})
        else:
            return render(request, 'runapp/startpage.html')
    else:
        return render(request, 'runapp/startpage.html')

def startinfo(request):
    if request.method == 'GET':
        res = request.GET.get('status')
        method = request.GET.get('name')
        if res == 'start':

            # complete()
            response =  HttpResponse("<h3>1. Начало " + method + " !</h3>")

        else:
            try:
                if method == 'Load':
                    startfirst()
                elif method == 'Key':
                    add_keys_img()
                elif method == 'Add':
                    complete()
                elif method == 'Close':
                    finish()
                response = HttpResponse("<h3>2.Окончание " + method + " </h3>")
            except BaseException as error:
                response = HttpResponse("<h3>2.Ошибка " + method + " </h3>")
                full_traceback = traceback.format_exc()
                print(full_traceback)
            # response = render(request,'runapp/phone-filter.html', {'phonenumbers':queryset})
    return response