import requests
from bs4 import BeautifulSoup
import xml
from testpage.models import Accounts
from runapp.models import Isue
from datetime import datetime
from .autorization import autorizen
from runapp.models import Fromproxy


def load_isue_sape():
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    # param a дозапись
    f = open('runapp\logfile.txt', 'a')
    f.write('Function load_isue: ' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\n')
    url = "http://api.pr.sape.ru/xmlrpc/"

    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = 'None'

    account_list = Accounts.objects.all()
    for user in account_list:
        user_name = user.name
        my_test = Accounts.objects.get(name=user_name)
        cookies = my_test.cookies_sape
        if cookies != 'None':
            # payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.login</methodName>\r\n  <params>\r\n    <param>\r\n        <value><string>" + token + "</string></value>\r\n    </param>\r\n  </params>\r\n</methodCall>"
            payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.site.adverts</methodName>\r\n  <params>\r\n    <param>\r\n        <value><struct><member><name>status_codes</name><value><int>5</int></value>\r\n    </member></struct></value>\r\n  </param>\r\n  <param><value><int>1</int></value>\r\n  </param>\r\n  </params>\r\n</methodCall>"

            headers = {
                'Content-Type': "text/xml",
                'Accept-Charset': "utf-8",
                'Cache-Control': "no-cache",
                'Cookie': cookies
            }
            response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
            # response = requests.post(url=url, data=payload, headers=headers)
            # print('Текст ответа: ', response.text)

            trace = BeautifulSoup(response.text, "xml")
            # Добавить при получении ошибки 403 переавторизировться иповторить попытку
            test = trace.find('fault')
            if test:
                autorizen()
                my_test = Accounts.objects.get(name=user_name)
                cookies = my_test.cookies_sape
                headers['Cookie'] = cookies
                response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
                trace = BeautifulSoup(response.text, "xml")

            root = trace.find_all('data')[0]
            isuecount = root.contents
            for isue in isuecount:
                book = isue.find('struct')
                isuenum = book.contents[0].find('value').get_text()
                isuetype = book.contents[1].find('value').get_text()
                site_link = book.contents[3].find('value').get_text()
                createdate = book.contents[23].find('value').get_text()
                ancor_href = book.contents[5].find('struct').contents[1].find('value').get_text()
                ancor_text = book.contents[5].find('struct').contents[2].find('value').get_text()
                ancor_tag = '<a href="' + ancor_href + '">' + ancor_text + '</a>'
                c = Isue.objects.count()
                # print(c)
                site_link = site_link.split('//')[1]
                second_test = Isue.objects.filter(platform_name='Sape').filter(id_isue=isuenum)
                if not second_test:
                    b = Isue(num=c + 1, id_isue=isuenum, type_isue=isuetype, site_platform=site_link,
                             date_create=createdate, anchor1=ancor_tag, anchor1_url=ancor_href, anchor1_text=ancor_text,
                             user_platform=user_name, platform_name='Sape')
                    if site_link == 'nanoplast.com.ua':
                        b.status_isue = 'Reword'
                    # b.currently = "shift"
                    b.save()
                    f.write(
                        user_name + ': ' + isuenum + ': ' + isuetype + ': ' + site_link + ': ' + createdate + ': ' + ancor_href + ': ' + ancor_text + '\n')
    f.write('\n')
    f.close()
