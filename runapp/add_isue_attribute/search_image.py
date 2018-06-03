import urllib3
from urllib.parse import quote
from bs4 import BeautifulSoup
import html5lib
import re
import random
from runapp.models import Fromproxy


def geturlimg(textimg):
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    urllib3.disable_warnings()
    if isproxy:
        proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
    else:
        proxy = urllib3.PoolManager(maxsize=10)
    # http = urllib3.PoolManager()
    keyword = textimg
    kw = quote(keyword)
    # https://www.google.com/search?q=%D0%B7%D0%BE%D0%BD%D1%82%D0%B8%D0%BA&tbas=0&tbm=isch&source=lnt&tbs=isz:m  &source=lnms&tbm=isch
    # page = proxy.request('GET','https://www.google.com.ua/search?q=%D0%BA%D0%B0%D0%BA+%D0%BE%D0%B4%D0%B5%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F+%D0%B7%D0%B8%D0%BC%D0%BE%D0%B9&source=lnms&tbm=isch',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    page = proxy.request('GET', 'https://www.google.com.ua/search?q=' + kw + '&tbas=0&tbm=isch&source=lnt&tbs=isz:m', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    trace = BeautifulSoup(page.data, "html5lib")
    result_block = trace.find_all('div', attrs={'class': 'rg_meta notranslate'})
    found_results = []
    # rank = 1
    for result in result_block:
        text = result.get_text()
        dct = eval(text)
        # print(dct['ou'])
        found_results.append(dct['ou'])
    # Поcле поллучения списка берем из него рандомный url
    my_sleep = random.randint(1, 10)
    return found_results[my_sleep]
