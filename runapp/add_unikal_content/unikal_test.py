# Тут будет проверка на уникальность
import requests
from bs4 import BeautifulSoup
import time
from runapp.models import Fromproxy

def getunikal(content):
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    cutcontent = content[:1477]
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = None
    url = "http://ahumor.org.ua/textapi.php?text=" + cutcontent
    headers = {
        'Content-Type': "text/xml",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache",
    }
    time.sleep(3)
    response = requests.get(url=url, headers=headers, proxies=proxies)
    time.sleep(2)
    trace = BeautifulSoup(response.text, "lxml")
    result_block = trace.find('p')
    tark = result_block.get_text()
    result = int(tark.split('.')[0])
    return result