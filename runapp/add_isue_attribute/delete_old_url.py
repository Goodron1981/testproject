import datetime

from runapp.models import GUrl_List


def deleteOU():
    mydate = datetime.date.today()
    thisyear = mydate.year
    thismonth = mydate.month
    thisday = mydate.day
    result = datetime.date(thisyear,thismonth-1,thisday)
    print(result)

    url_list = GUrl_List.objects.filter(create_date__lte=result)
    for url in url_list:
        url.delete()