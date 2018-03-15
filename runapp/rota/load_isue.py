import requests
from bs4 import BeautifulSoup
import lxml
from testpage.models import Accounts
from runapp.models import Isue
from datetime import datetime


def load_isue_rota():
    now = datetime.now()
    #param a дозапись
    f = open('runapp\logfile.txt', 'a')
    f.write('Function load_isue_rota: ' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\n')

    proxies = {
      'http': 'http://10.18.7.6:3128',
      'https': 'http://10.18.7.6:3128',
    }

    acount_list = Accounts.objects.all()

    for user in acount_list:
        user_name = user.name
        apikey = user.apikey_rota
        if apikey != 'None':
            url = "https://api.rotapost.ru/Task/Webmaster?Status=ToDo&ApiKey=" + apikey
            #print(url + '\n')
            headers = {
                'Content-Type': "text/xml",
                'Accept-Charset': "utf-8",
                'Cache-Control': "no-cache"
                }
            response = requests.get(url=url, headers=headers, proxies=proxies)
            #response = requests.post(url=url, data=payload, headers=headers)
            #print('Текст ответа: ', response.text)

            trace = BeautifulSoup(response.text, "lxml")
            result_block = trace.find('success')
            validate = result_block.get_text()
            if validate:
                idisues = trace.find_all('id')
                typeisues = trace.find_all('type')
                siteisues = trace.find_all('site')
                cuisues = trace.find_all('checkurl')
                cdisues = trace.find_all('createdate')
                print('\n')
                for isue in idisue:
                    print(isue.get_text())
                    #print(str(idisue), + '\n')
                    '''
                    isuenum = book.contents[0].find('value').get_text()
                    isuetype = book.contents[1].find('value').get_text()
                    site_link = book.contents[3].find('value').get_text()
                    createdate = book.contents[23].find('value').get_text()
                    ancor_href = book.contents[5].find('struct').contents[1].find('value').get_text()
                    ancor_text = book.contents[5].find('struct').contents[2].find('value').get_text()
                    ancor_tag = '<a href="'+ ancor_href +'">' + ancor_text + '</a>'
                    c = Isue.objects.count()
                    #print(c)
                    #site_link = site_link.split('//')[1]
                    b = Isue(num = c+1, id_isue = isuenum, type_isue = isuetype, site_platform = site_link, date_create = createdate, anchor1 = ancor_tag, anchor1_url = ancor_href, anchor1_text = ancor_text, user_platform = user_name, platform_name = 'Sape')
                    #b.currently = "shift"
                    b.save()
                    f.write(user_name + ': ' + isuenum + ': ' + isuetype + ': ' + site_link + ': ' + createdate + ': ' + ancor_href + ': ' + ancor_text + '\n')
                    '''
            else:
                print(user_name + ': Error autorization')
                f.write(user_name + ': Error autorization' + '\n')
    f.write('\n')
    f.close()
