from django.contrib import admin

# Register your models here.
from testpage.models import Urls, Accounts, AccountsAdmin, UrlsAdmin
from tutorial.models import Person

admin.site.register(Urls, UrlsAdmin)
admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Person)
