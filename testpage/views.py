from django.shortcuts import get_object_or_404, render
from  django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from testpage.models import Urls
from runapp.models import Fromproxy

import urllib3
from bs4 import BeautifulSoup
import lxml
import html5lib
import re

'''
# Create your views here.
def index(request):
    return HttpResponse("<h3>Привет Мир!")
'''
stoper = 2+2
wendor = 'bus'
def index(request):
    return render(request, 'testpage/mainpage.html', {wendor:stoper})

def detail(request):
    pk=request.POST['choice']
    return render(request, 'testpage/mainpage.html', {'topper': pk})

def search_form(request):
    return render_to_response(request,'testpage/mainpage.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


def get_parse(request):
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    pk=request.POST['choice']
    c = Urls.objects.count()
    #print(c)
    b = Urls(num = c+1, url=pk)
    #b.currently = "shift"
    b.save()
    urllib3.disable_warnings()
    if isproxy:
        proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
    else:
        proxy = urllib3.PoolManager(maxsize=10)
    # proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
    page = proxy.request('GET', pk, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    trace = BeautifulSoup(page.data, "html5lib")
    bots = trace.find_all('body')[0]
    bebots = bots.get_text()
    bush = bebots.lower()
    startserch = bush.find('комментар')
    bebots = bebots[:startserch]
    pattern = re.compile(r'[А-Я].+[!.?]')
    pattern2 = re.compile(r'\s{2}')
    #sloer = re.search(r'\.', bots.get_text())
    cholks = pattern2.split(bebots)
    f = open('test.txt', 'w')
    #str = "  "
    mytext = ""
    #print(cholks)
    for cholk in cholks:
        sloer = pattern.findall(cholk)
        for mark in sloer:
            for wen in mark:
                if wen !='\u2192' and wen !='\xd7':
                    mytext = mytext + wen
            mytext = mytext + ' '
        mytext = mytext + ' \n'
    f.write(mytext)
    f.close()
    mytext = mytext.replace(".", ". ")
    mytext = re.sub(" \d+\.", "", mytext)
    #исправляем склеивание предложений в переносах
    pattern3 = re.compile(r'[а-яё)][А-ЯЁ«]')
    boki = pattern3.findall(mytext)
    for bet in boki:
        wix = bet[:1] + ". " + bet[1:]
        mytext = mytext.replace(bet, wix)
    #исправляем попадание неверных знаков
    pattern4 = re.compile(r'[\w][^\s\w][\w]')
    boki = pattern4.findall(mytext)
    for bet in boki:
        wix = bet[:2] + " " + bet[2:]
        mytext = mytext.replace(bet, wix)

    validtext = re.split(r'[.!?]', mytext)
    pattern5 = re.compile(r'[а-яё]+')
    group = ""
    for peace in validtext:
        testvalid = pattern5.findall(peace)
        if len(testvalid)>4:
            group = group + peace + '.'
    return render(request, 'testpage/mainpage.html', {'topper': group, 'inval':pk})
