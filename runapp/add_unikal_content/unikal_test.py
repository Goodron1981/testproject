# Тут будет проверка на уникальность
import requests
from bs4 import BeautifulSoup
import time

def getunikal(content):
    cutcontent = content[:1477]
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    url = "http://ahumor.org.ua/textapi.php?text=" + cutcontent
    headers = {
        'Content-Type': "text/xml",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache",
    }
    time.sleep(2)
    response = requests.get(url=url, headers=headers, proxies=proxies)
    trace = BeautifulSoup(response.text, "lxml")
    result_block = trace.find('p')
    tark = result_block.get_text()
    result = int(tark.split('.')[0])
    return result