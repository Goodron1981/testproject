# Тут будет закрытие заявок рота
import requests
from bs4 import BeautifulSoup
from testpage.models import Accounts
from runapp.rota.autorization import autorizen
from runapp.models import Fromproxy

def closerota(isue):
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    username = isue.user_platform
    acount = Accounts.objects.get(name=username)
    apikey = acount.apikey_rota
    idisue = str(isue.id_isue)
    urlresult = isue.public_url
    url = "https://api.rotapost.ru/Task/Complete?TaskId=" + idisue + "&CheckUrl=" + urlresult + "&ApiKey=" + apikey
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = None
    headers = {
            'Content-Type': "text/xml",
            'Accept-Charset': "utf-8",
            'Cache-Control': "no-cache"
        }
    response = requests.post(url=url, headers=headers, proxies=proxies)
    trace = BeautifulSoup(response.text, "lxml")
    result_block = trace.find('success')
    validate = result_block.get_text()
    if validate == 'false':
        autorizen()
        acount = Accounts.objects.get(name=username)
        apikey = acount.apikey_rota
        url = "https://api.rotapost.ru/Task/Complete?TaskId=" + idisue + "&CheckUrl=" + urlresult + "&ApiKey=" + apikey
        response = requests.post(url=url, headers=headers, proxies=proxies)
        trace = BeautifulSoup(response.text, "lxml")
        result_block = trace.find('success')
        validate = result_block.get_text()
        if validate == 'false':
            result_block = trace.find_all('description')
            result = result_block[0].get_text()
        else:
            result = "Закрыто"
    else:
        result = "Закрыто"
    return result