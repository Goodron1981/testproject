import requests
from bs4 import BeautifulSoup
from .autorization import autorizen
from testpage.models import Accounts
from runapp.models import Isue
from datetime import datetime
from runapp.models import Fromproxy


def load_isue_rota():
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    now = datetime.now()
    #param a дозапись
    f = open('runapp\logfile.txt', 'a')
    f.write('Function load_isue_rota: ' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\n')

    proxies = {
      'http': 'http://10.18.7.6:3128',
      'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = 'None'

    acount_list = Accounts.objects.all()

    for user in acount_list:
        user_name = user.name
        my_test = Accounts.objects.get(name=user_name)
        apikey = my_test.apikey_rota
        # apikey = user.apikey_rota
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
            if validate == 'false':
                autorizen()
                my_test = Accounts.objects.get(name=user_name)
                apikey = my_test.apikey_rota
                url = "https://api.rotapost.ru/Task/Webmaster?Status=ToDo&ApiKey=" + apikey
                response = requests.get(url=url, headers=headers, proxies=proxies)
                trace = BeautifulSoup(response.text, "lxml")

            idisues = trace.find_all('id')
            typeisues = trace.find_all('type')
            textisues = trace.find_all('text')
            siteisues = trace.find_all('site')
            cuisues = trace.find_all('checkurl')
            cdisues = trace.find_all('createdate')
            print('\n')
            cost = 0
            for isue in idisues:
                idisue = idisues[cost].get_text()
                typeisue = typeisues[cost].get_text()
                textisue = textisues[cost].get_text()
                sitetisue = siteisues[cost].get_text()
                cuisue = cuisues[cost].get_text()
                if not cuisue:
                    cuisue = "None"
                cdisue = cdisues[cost].next

                if typeisue == "Postovoi":
                    starturl = textisue.find('href="') + 6
                    finurl = textisue.find('"', starturl)
                    ancor_href = textisue[starturl:finurl]

                    starttext = textisue.find('>') + 1
                    fintext = textisue.find('</a>', starttext)
                    ancor_text = textisue[starttext:fintext]
                else:
                    ancor_href = "None"
                    ancor_text = "None"

                cost+=1
                c = Isue.objects.count()
                second_test = Isue.objects.filter(platform_name = 'Rota').filter(id_isue = idisue)
                if not second_test:
                    b = Isue(num = c+1, id_isue = idisue, type_isue = typeisue, site_platform = sitetisue, date_create = cdisue, anchor1 = textisue, anchor1_url = ancor_href, anchor1_text = ancor_text, check_url_rota = cuisue, user_platform = user_name, platform_name = 'Rota')
                    if typeisue == 'Post' or typeisue == 'PressRelease' or cuisue != 'None' or sitetisue == 'nanoplast.com.ua':
                        b.status_isue = 'Reword'
                    b.save()
                    f.write(user_name + ': ' + idisue + ': ' + typeisue + ': ' + sitetisue + ': ' + cdisue + ': ' + ancor_href + ': ' + ancor_text + '\n')
    f.write('\n')
    f.close()
