# Тут поиск и перебор урлов по ключевой фразе
import urllib3
from bs4 import BeautifulSoup
import html5lib
from urllib.parse import quote
from runapp.models import Fromproxy

def geturls(serchtext, page):
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    urllib3.disable_warnings()
    if isproxy:
        proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
    else:
        proxy = urllib3.PoolManager(maxsize=10)
    # proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
    # http = urllib3.PoolManager()
    keyword = serchtext
    kw = quote(keyword)
    amount = page * 10 + 10
    page = proxy.request('GET','https://www.google.com.ua/search?q=' + kw + '&start=' + str(amount),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    trace = BeautifulSoup(page.data, "html5lib")
    result_block = trace.find_all('div', attrs={'class': 'g'})
    found_results = []
    for result in result_block:
        link = result.find('a', href=True)
        if link:
            link = link['href']
            if link != '#':
                found_results.append(link)
    return found_results