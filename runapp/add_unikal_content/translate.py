# Тут будет выполнятся перевод текста
import requests
from bs4 import BeautifulSoup
from runapp.models import Fromproxy

def translatecont(content):
    isproxy1 = Fromproxy.objects.get(pk=1).proxy_val
    proxies1 = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    isproxy2 = Fromproxy.objects.get(pk=3).proxy_val
    proxies2 = {
        'http': 'http://213.168.37.86:8080',
        'https': 'http://213.168.37.86:8080',
    }
    if isproxy1:
        proxies = proxies1
    elif isproxy2:
        proxies = proxies2
    url = "https://translate.yandex.net/api/v1.5/tr/translate?key=trnsl.1.1.20170804T113914Z.99f7ddfc45f28e25.1963be741f6352a1c038fb90c84e8b069cc868ba&format=html&lang=uk&text=" + content
    headers = {
        'Content-Type': "text/xml",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache",
    }
    response = requests.get(url=url, timeout = 2000, headers=headers, proxies=proxies)
    trace = BeautifulSoup(response.text, "lxml")
    result_block = trace.find('text')
    if result_block:
        validate = result_block.get_text()
    else:
        validate = trace.find_all('error')
        print(validate[0].find("message"))
    return validate