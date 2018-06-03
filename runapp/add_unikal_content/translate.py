# Тут будет выполнятся перевод текста
import requests
from bs4 import BeautifulSoup
from runapp.models import Fromproxy

def translatecont(content):
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = None
    url = "https://translate.yandex.net/api/v1.5/tr/translate?key=trnsl.1.1.20170804T113914Z.99f7ddfc45f28e25.1963be741f6352a1c038fb90c84e8b069cc868ba&format=html&lang=uk&text=" + content
    headers = {
        'Content-Type': "text/xml",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache",
    }
    response = requests.get(url=url, headers=headers, proxies=proxies)
    trace = BeautifulSoup(response.text, "lxml")
    result_block = trace.find('text')
    if result_block:
        validate = result_block.get_text()
    else:
        validate = trace.find_all('error')
        print(validate[0].find("message"))
    return validate