import traceback
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from runapp.add_isue_attribute.search_keys import add_keys_img
from runapp.mainapp.compliter import complete
from runapp.mainapp.finisher import finish
from runapp.mainapp.starter import startfirst
from testpage.models import Urls
from runapp.add_isue_attribute.list_admin import add_last_key


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

def addkeys(request):
    if request.method == 'GET':
        res = request.GET.get('status')
        method = request.GET.get('name')
        root = request.GET.get('root')
        img = request.GET.get('img')
        keyword = request.GET.get('keyword')
        exroot = request.GET.get('exroot')
        eximg = request.GET.get('eximg')
        exkeyword = request.GET.get('exkeyword')
        if exroot == '' or eximg == '' or exkeyword == '':
            exroot = eximg = exkeyword = None
        if res == 'start':
            # complete()
            response =  HttpResponse("<h3>1. Начало " + method + " !</h3>")

        else:
            try:
                snop = add_last_key(root, img, keyword, exroot, eximg, exkeyword)
                if snop:
                    response = HttpResponse("<h3>2.Ключ '" + root + "' добавлен!</h3>")
                else:
                    response = HttpResponse("<h3>2.Ключ  '" + root + "'  уже существует!</h3>")
            except BaseException as error:
                response = HttpResponse("<h3>2.Ошибка " + method + " </h3>")
                full_traceback = traceback.format_exc()
                print(full_traceback)
            # response = render(request,'runapp/phone-filter.html', {'phonenumbers':queryset})
    return response