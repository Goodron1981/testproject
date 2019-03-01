# Тут будет выполнятся перевод текста
import traceback

import requests

from bs4 import BeautifulSoup
from runapp.models import Fromproxy
from runapp.models import Proxy_List
import time


def translatecont(content):

    '''
    isproxy1 = Fromproxy.objects.get(pk=1).proxy_val
    proxies1 = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    isproxy2 = Fromproxy.objects.get(pk=3).proxy_val
    proxies2 = {
        'http': 'http://200.41.187.122:3130',
        'https': 'http://200.41.187.122:3130',
    }
    #TODO add some useful code here
    # 188.138.195.178:8080 - не работает
    # 213.136.105.54:80 - не работает
    # 213.168.37.86:8080 - проверялась - глючит
    # 185.85.162.32:72 - не работает
    # 200.41.187.122:3130
    # 186.215.199.245:20183 - неработает
    if isproxy1:
        proxies = proxies1
    elif isproxy2:
        proxies = proxies2

    '''
    url = "https://translate.yandex.net/api/v1.5/tr/translate?key=trnsl.1.1.20170804T113914Z.99f7ddfc45f28e25.1963be741f6352a1c038fb90c84e8b069cc868ba&format=html&lang=uk&text=" + content
    headers = {
        'Content-Type': "text/xml",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache",
    }
    proxylist = Proxy_List.objects.order_by("num")
    for myproxy in proxylist:
        try:
            time.sleep(10)
            proxies2 = {
                'http': 'http://' + str(myproxy.proxy_host),
                'https': 'http://' + str(myproxy.proxy_host),
            }
            print(myproxy.proxy_host)
            response = requests.get(url=url, timeout=5000, headers=headers, proxies=proxies2, verify=False)
            break
        except BaseException as error:
            full_traceback = traceback.format_exc()
            print(full_traceback)
            print("Ошибка", myproxy.proxy_host)
            gotoend()
            continue

    trace = BeautifulSoup(response.text, "lxml")
    result_block = trace.find('text')
    if result_block:
        validate = result_block.get_text()
    else:
        validate = trace.find_all('error')
        print(validate[0].find("message"))
    return validate

def gotoend():
    proxylist = Proxy_List.objects.order_by("num")
    lenlist = len(proxylist)
    firstelem = proxylist.get(num=1)
    firstelem.num = lenlist
    firstelem.save()
    for myelem in proxylist:
        if myelem.num > 1:
           oldnum = myelem.num
           myelem.num = oldnum - 1
           myelem.save()
