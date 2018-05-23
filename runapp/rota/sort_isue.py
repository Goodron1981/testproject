from runapp.models import Isue

def sortallisues():
    isue_list = Isue.objects.all().order_by('date_create')
    c = 1
    for isue in isue_list:
        isue.num = c
        isue.save()
        c = c + 1


