from django.db import models
from django.contrib import admin

class Urls(models.Model):
    num = models.IntegerField(default = 1)
    url = models.URLField()
    adddate = models.DateTimeField(auto_now_add=True)
    #tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return str(self.num)

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('num', 'url','adddate')
    ordering = ('num',)


class Accounts(models.Model):
    name = models.CharField(max_length=10, default = 'None')
    cookies_sape = models.CharField(max_length=100, default = 'None')
    token_sape = models.TextField()
    url_rota = models.URLField(max_length=200, default = 'None')
    apikey_rota = models.CharField(max_length=40, default = 'None')
    auth_blog = models.CharField(max_length=100, default = 'None')
    iduser_blog = models.CharField(max_length=10, default = 'None')
    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('name', 'cookies_sape', 'token_sape', 'url_rota', 'apikey_rota', 'auth_blog', 'iduser_blog')
    ordering = ('name',)
