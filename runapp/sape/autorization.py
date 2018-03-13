import requests
from bs4 import BeautifulSoup
import lxml
from testpage.models import Accounts
from datetime import datetime


def autorizen():
    now = datetime.now()
    #param a дозапись
    f = open('runapp\sape\logfile.txt', 'a')
    f.write('Function autorizen: ' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\n')
    url = "http://api.pr.sape.ru/xmlrpc/"

    proxies = {
      'http': 'http://10.18.7.6:3128',
      'https': 'http://10.18.7.6:3128',
    }

    acount_list = Accounts.objects.all()
    for user in acount_list:
        user_name = user.name
        token = user.token_sape
        if token != 'None':
            payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.login</methodName>\r\n  <params>\r\n    <param>\r\n        <value><string>" + token + "</string></value>\r\n    </param>\r\n  </params>\r\n</methodCall>"
            headers = {
                'Content-Type': "text/xml",
                'Accept-Charset': "utf-8",
                'Cache-Control': "no-cache",
                }
            response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
            #response = requests.post(url=url, data=payload, headers=headers)
            #print('Текст ответа: ', response.text)
            trace = BeautifulSoup(response.text, "lxml")
            result_block = trace.find_all('int')
            validate = result_block[0].get_text()
            if validate != '403':
                cookies = response.headers['Set-Cookie']
                print(user_name + ': ' + validate + ': ' + cookies)
                f.write(user_name + ': ' + validate + ': ' + cookies+ '\n')
                user.cookies_sape = cookies
                user.save()
            else:
                print(user_name + ': Error: ' + validate + ': ' + cookies)
                f.write(user_name + ': Error: ' + validate + ': ' + cookies)
    f.write('\n')
    f.close()
