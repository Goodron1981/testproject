# tutorial/tables.py
import django_tables2 as tables
from .models import Person
from testpage.models import Urls
from testpage.models import Accounts
from runapp.models import Isue
from runapp.models import Keys_List

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap.html'

class UrlsTable(tables.Table):
    class Meta:
        model = Urls
        template_name = 'django_tables2/bootstrap.html'

class AccountsTable(tables.Table):
    class Meta:
        model = Accounts
        template_name = 'django_tables2/bootstrap.html'

class IsueTable(tables.Table):
    class Meta:
        model = Isue
        template_name = 'django_tables2/bootstrap.html'

class Keys_ListTable(tables.Table):
    class Meta:
        model = Keys_List
        template_name = 'django_tables2/bootstrap.html'
