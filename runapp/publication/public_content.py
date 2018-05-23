# Тут будет публикация и получение результата (урл картинки) и статус публикации
from json import JSONDecodeError

from runapp.models import Isue
import requests
from runapp.add_unikal_content.translate import translatecont
import json


def publilconent(content, isue_num):
    isue = Isue.objects.get(num=isue_num)
    # print(isue.num)
    ank1 = isue.anchor1
    ank2 = isue.anchor2
    name_platform = isue.site_platform
    content_title = translatecont(isue.key_words)
    urlofimg = isue.img_url
    if ank2 != "None":
        secondankor = "Найбільший вибір можна знайти на " + ank2 + ". "
    else:
        secondankor = ""

    peacelen = int(len(content)/3)
    startfirstpart = content.rfind('. ', 0, peacelen)
    finfirstpart = content.find('. ', peacelen)
    # не срабатывает rfind
    renstart =  peacelen - startfirstpart
    renfinish =  finfirstpart - peacelen
    if renstart - renfinish > 0:
        firstpart = finfirstpart
    else:
        firstpart = startfirstpart

    startsecondpart = content.rfind('. ', peacelen, (peacelen*2) - 1)
    finsecondpart = content.find('. ', (peacelen*2) + 1)
    renstart = (peacelen*2) - startsecondpart
    renfinish = finsecondpart - (peacelen*2)
    if renstart - renfinish > 0:
        secondpart = finsecondpart
    else:
        secondpart = startsecondpart

    # resulttext = ' \\t' + content[:firstpart + 1] + ' Також Ви можете знайти все необхідне на ресурсі ' + ank1 + '. \\r' + content[firstpart + 2:secondpart + 1] + secondankor +  '\\r' + content[secondpart + 2:]
    resulttext = ' \\t' + content[:firstpart + 1] + ' Також Ви можете знайти все необхідне на ресурсі ' + ank1 + '. \\r'+ content[firstpart + 2:secondpart + 1] + secondankor +  '\\r' + content[secondpart + 2:]
    soop = '[caption id="" align="" aligncenter"" width="350"]<img src="' + urlofimg + '" alt="" width="350" height="300" /> ' + content_title + '[/caption]' + '\\r' + resulttext
    print(soop)
    # Дальше публикация
    mytext = soop.replace('"', '\\"')


    url = "http://" + name_platform + "/wp-json/wp/v2/pages"

    # payload = "{\"title\":" + content_title + ",\n\"content\":" + resulttext + ",\n\"status\":\"publish\"}"
    poosk = 'Сложный текст.'
    payload = "{\"title\":\"" + content_title + "\",\n\"content\":\"" + mytext + "\",\n\"status\":\"publish\"}"
    body = payload.encode('utf-8')
    headers = {
        'Authorization': "Basic bWF4d2VsaGVscDo6YmRqbmpyODk",
        'Content-Type': "application/json",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache"
        }

    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }

    response = requests.post(url=url, data=body, headers=headers, proxies=proxies)
    if response.status_code == 201:
        parselist = json.loads(response.text)
        result = parselist.get('link','errorpublic')
    else:
        result = 'errorpublic'
        # except JSONDecodeError:
    # return parselist.get('link')
    return result

