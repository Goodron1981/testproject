from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
'''
# Create your views here.
def index(request):
    return HttpResponse("<h3>Привет Мир!")
'''
stoper = 2+2
wendor = 'bus'
def index(request):
    return render(request, 'testpage/mainpage.html', {wendor:stoper})


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
