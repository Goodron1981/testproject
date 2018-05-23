# Для закрытия заявок Сап
import requests
from bs4 import BeautifulSoup
from testpage.models import Accounts
from runapp.sape.autorization import autorizen

def closesape(isue):
    username = isue.user_platform
    acount = Accounts.objects.get(name=username)
    cookies = acount.cookies_sape
    idisue = str(isue.id_isue)
    urlresult = isue.public_url
    url = "http://api.pr.sape.ru/xmlrpc/"
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    if cookies != 'None':
        payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.advert.place</methodName>\r\n  <params>\r\n    <param>\r\n        <value><int>" + idisue + "</int></value>\r\n    </param>\r\n    <param>\r\n        <value><string>" + urlresult + "</string></value>\r\n    </param>\r\n  </params>\r\n</methodCall>"
        headers = {
            'Content-Type': "text/xml",
            'Accept-Charset': "utf-8",
            'Cache-Control': "no-cache",
            'Cookie': cookies
        }
        comment = 'Добрый день. \nВаша заявка выполнена. \nЯ написал Вам ТЕМАТИЧЕСКУЮ, уникальную статью, обращайтесь, буду рад дальнейшему сотрудничеству у меня много качественных сайтов.'
        response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
        validate = response.text.find('faultCode')
        if validate > 0:
            autorizen()
            acount = Accounts.objects.get(name=username)
            cookies = acount.cookies_sape
            headers['Cookie'] = cookies
            response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
            validate = response.text.find('faultCode')
            if validate > 0:
                trace = BeautifulSoup(response.text, "xml")
                result_block = trace.find_all('string')
                result = result_block[0].get_text()
            else:
                result = "Закрыто"
                payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.advert.add_comment</methodName>\r\n  <params>\r\n    <param>\r\n        <value><int>" + idisue + "</int></value>\r\n    </param>\r\n    <param>\r\n        <value><string>" + comment + "</string></value>\r\n    </param>\r\n    <param>\r\n        <value><string>all</string></value>\r\n    </param>\r\n  </params>\r\n</methodCall>"
                payload = payload.encode('utf-8')
                response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
                response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
        else:
            result = "Закрыто"
            payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.advert.add_comment</methodName>\r\n  <params>\r\n    <param>\r\n        <value><int>" + idisue + "</int></value>\r\n    </param>\r\n    <param>\r\n        <value><string>" + comment + "</string></value>\r\n    </param>\r\n    <param>\r\n        <value><string>all</string></value>\r\n    </param>\r\n  </params>\r\n</methodCall>"
            payload = payload.encode('utf-8')
            response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
            response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
    return result