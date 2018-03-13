import requests
from bs4 import BeautifulSoup
import xml
from testpage.models import Accounts
from datetime import datetime


def load_isue():
    now = datetime.now()
    #param a дозапись
    f = open('runapp\sape\logfile.txt', 'a')
    f.write('Function load_isue: ' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\n')
    url = "http://api.pr.sape.ru/xmlrpc/"

    proxies = {
      'http': 'http://10.18.7.6:3128',
      'https': 'http://10.18.7.6:3128',
    }

    acount_list = Accounts.objects.all()
    for user in acount_list:
        user_name = user.name
        cookies = user.cookies_sape
        if cookies != 'None':
            #payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.login</methodName>\r\n  <params>\r\n    <param>\r\n        <value><string>" + token + "</string></value>\r\n    </param>\r\n  </params>\r\n</methodCall>"
            payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n  <methodName>sape_pr.site.adverts</methodName>\r\n  <params>\r\n    <param>\r\n        <value><struct><member><name>status_codes</name><value><int>5</int></value>\r\n    </member></struct></value>\r\n  </param>\r\n  <param><value><int>1</int></value>\r\n  </param>\r\n  </params>\r\n</methodCall>"

            headers = {
                'Content-Type': "text/xml",
                'Accept-Charset': "utf-8",
                'Cache-Control': "no-cache",
                'Cookie': cookies
                }
            response = requests.post(url=url, data=payload, headers=headers, proxies=proxies)
            #response = requests.post(url=url, data=payload, headers=headers)
            #print('Текст ответа: ', response.text)

            trace = BeautifulSoup(response.text, "xml")
            root = trace.find_all('data')[0]
            isuecount = root.contents
            for isue in isuecount:
                book = isue.find('struct')
                isuenum = book.contents[0].find('value').get_text()
                isuetype = book.contents[1].find('value').get_text()
                site_link = book.contents[3].find('value').get_text()
                date_create = book.contents[23].find('value').get_text()
                ancor_href = book.contents[5].find('struct').contents[1].find('value').get_text()
                ancor_text = book.contents[5].find('struct').contents[2].find('value').get_text()
                print('isuenum: '+ isuenum + '\n')
                print('isuetype: '+ isuetype + '\n')
                print('site_link: '+ site_link + '\n')
                print('date_create: '+ date_create + '\n')
                print('ancor_href: '+ ancor_href + '\n')
                print('ancor_text: '+ ancor_text + '\n')
            '''
            isuenum = Trim(structvalue.ChildNodes.Item(0).SelectSingleNode("value").Text)
            isuetype = Trim(structvalue.ChildNodes.Item(1).SelectSingleNode("value").Text)
            site_link = Trim(structvalue.ChildNodes.Item(3).SelectSingleNode("value").Text)
ancor_href = Trim(structvalue.ChildNodes.Item(5).SelectSingleNode("value/array/data/value/struct").ChildNodes.Item(1).SelectSingleNode("value").Text)
ancor_text = Trim(structvalue.ChildNodes.Item(5).SelectSingleNode("value/array/data/value/struct").ChildNodes.Item(2).SelectSingleNode("value").Text)
            date_create = Trim(structvalue.ChildNodes.Item(23).SelectSingleNode("value").Text)

            for chalk in result_block:
                fato = chalk.find_next_sibling('value')
                print(fato)

            for chalk in result_block:
                #validate = result_block[0].get_text()
                print(chalk.next_sibling.get_text()+'\n')
                #f.write(trace)

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
    '''
