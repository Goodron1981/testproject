import urllib3
from bs4 import BeautifulSoup
# from urllib3.exceptions import MaxRetryError, SSLError
# from requests.exceptions import SSLError
from runapp.models import Isue
from urllib.parse import quote
import requests
import lxml
import html5lib
import re
from runapp.models import Fromproxy

def parser_attr():
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    isue_list = Isue.objects.filter(status_isue='New').order_by('num')
    # isue_list = Isue.objects.all()
    for isue in isue_list:
        search_url = quote(isue.anchor1_url, safe='/,:')
        # search_url = isue.anchor1_url
        ''''
        urllib3.disable_warnings()
        proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=20)
        '''
        #

        proxies = {
            'http': 'http://10.18.7.6:3128',
            'https': 'http://10.18.7.6:3128',
        }
        if not isproxy:
            proxies = None

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# requests.exceptions.ProxyError
        try:
            response = requests.get(url=search_url, headers=headers, proxies=proxies, verify=False)
        except:
            mytext = "Bad request"
        else:
            goop = response.encoding
            mytext = response.text
        # response = requests.post(url=url, data=payload, headers=headers)
        # print('Текст ответа: ', response.text)
        if goop and goop.lower() != 'utf-8':
            try:
                mytext = mytext.encode(goop).decode('windows-1251')
            except UnicodeDecodeError:
                mytext = response.text
        trace = BeautifulSoup(mytext, "html5lib")
        ''''
        page = proxy.request('GET', search_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
        trace = BeautifulSoup(page.data, "html5lib")
        
        wintest = trace.find('head')
        wintext = wintest.get_text()
        winlower = wintext.lower()
        mark = winlower.find('windows-1251')
        if mark >0:
            foot  = response.text
            foot.encoding = 'windows-1251'
            trace = BeautifulSoup(foot, "html5lib")
        '''
        bots = trace.find_all('title')
        if bots:
            bebots = bots[0].get_text()
            isue.title_parse = bebots
            isue.save()
        bots2 = trace.find('meta', attrs={'name':'keywords'})
        bots3 = trace.find('meta', attrs={'name': 'description'})
        if bots2:
            keys = bots2['content']
            isue.keywords_parse = keys
            isue.save()
        elif bots3:
            keys = bots3['content']
            isue.keywords_parse = keys
            isue.save()
