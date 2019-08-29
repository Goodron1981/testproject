# Тут будет проверка на уникальность
import requests
import json

def getunikal(content):
    url = "https://content-watch.ru/public/api/"
    cutcontent = content[:1477]
    payload = {
        'action': 'CHECK_TEXT',
        'text': cutcontent,
        'key': 'Y1QPlbw8P4ssZ1x',
        'test': 0,
    }

    # body = payload.encode('utf-8')
    proxies = None

    response = requests.post(url=url, data=payload, proxies=proxies)
    if response.status_code == 200:
        parselist = json.loads(response.text)
        tark = parselist.get('percent', 'errortext')
        result = int(tark.split('.')[0])
        errortext = parselist.get('error')
        print(errortext)
        if result == "errortext":
            result = errortext
    else:
        result = response.text

    return result