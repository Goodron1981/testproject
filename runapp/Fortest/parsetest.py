# Тут выполняется парсинг страници
import urllib3
from bs4 import BeautifulSoup
import re
from runapp.models import Excludespage
import time
from runapp.models import Fromproxy

def getcontent(searchurl):
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    urllib3.disable_warnings()
    if isproxy:
        proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
    else:
        proxy = urllib3.PoolManager(maxsize=10)
    # proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
    try:
        page = proxy.request('GET', searchurl, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})

    except:
        print("Connection refused by the server..")
        bebots = 'Bad request'

    else:
        # 1. Преобразовать responsetext в Dom структуру Html
        trace = BeautifulSoup(page.data, "html5lib")
        # 2. Отыскать тег body
        bots = trace.find_all('body')[0]
        # 3. Извлечь из body весь текст
        bebots = bots.get_text()

    # bebots = bots.get_text()
    bush = bebots.lower()
    # сюда добавить проверку на исключающие страницу слова( те что указівают на явнонеуникальный или неподходящий текст)
    exwordlist = Excludespage.objects.all()
    for exword in exwordlist:
        serchword = '\\b' + exword.ex_page + '\\b'
        exvalid = re.search(serchword, bush)
        if exvalid:
            bebots = "Bad text."
            break
    else:
        partens = trace.find_all('p')
        for block in partens:
            if len(block.get_text()) > 99:
                bebots = bebots + " " + block.get_text()

    # 1 Изымаем параграфы


    # удаляем названия с большой буквы на кирилице в фигурных кавычках
    bebots = re.sub("\s*«[А-ЯЁ].*»\s*", " ", bebots)
    # удаляем названия с большой буквы на кирилице в обычных кавычках
    bebots = re.sub('\s*"[А-ЯЁ].*"\s*', ' ', bebots)

    pattern = re.compile(r'[А-Я].+[!.?]')
    pattern2 = re.compile(r'\s{2}')
    cholks = pattern2.split(bebots)
    mytext = ""
    for cholk in cholks:
        sloer = pattern.findall(cholk)
        for mark in sloer:
            for wen in mark:
                if wen !='\u2192' and wen !='\xd7':
                    mytext = mytext + wen
            mytext = mytext + ' '
        mytext = mytext + ' \n'
    mytext = mytext.replace(".", ". ")
    mytext = re.sub(" \d+\.", "", mytext)
    # исправляем склеивание предложений в переносах
    pattern3 = re.compile(r'[а-яё)][А-ЯЁ«]')
    boki = pattern3.findall(mytext)
    for bet in boki:
        wix = bet[:1] + ". " + bet[1:]
        mytext = mytext.replace(bet, wix)
    # исправляем попадание неверных знаков
    pattern4 = re.compile(r'[\w][^\s\w][\w]')
    boki = pattern4.findall(mytext)
    for bet in boki:
        wix = bet[:2] + " " + bet[2:]
        mytext = mytext.replace(bet, wix)

    validtext = re.split(r'[.!?]', mytext)
    pattern5 = re.compile(r'[а-яё]+')
    group = ""
    for peace in validtext:
        testvalid = pattern5.findall(peace)
        if len(testvalid)>4:
            group = group + peace + '.'
        pattern6 = re.compile(r'\s{2,}')
        result = pattern6.sub(' ',group)
    return result