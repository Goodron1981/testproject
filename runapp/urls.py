from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.startpage, name='startpage'),
    url(r'startinfo', views.startinfo, name='startinfo'),
    url(r'subpage', views.subpage, name='subpage'),
    url(r'phone-filter', views.phone_filter, name='phone-filter'),
    url(r'runner-filter', views.runner_filter, name='runner-filter'),
]
