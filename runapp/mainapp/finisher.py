from runapp.models import Isue
from runapp.close_isue.close_isue_sape import closesape
from runapp.close_isue.close_isue_rota import closerota
import time

def finish():
    isue_list = Isue.objects.filter(status_isue='AddUnikal').exclude(public_url = 'errorpublic')
    for isue in isue_list:
        time.sleep(3)
        platforme = isue.platform_name
        if platforme == 'Sape':
            closeresulte = closesape(isue)
        else:
            closeresulte = closerota(isue)

        if closeresulte == 'Закрыто':
            isue.status_isue = 'Closed'
            isue.save()
        else:
            isue.status_isue = closeresulte
            isue.save()

