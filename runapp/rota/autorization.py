import requests
from bs4 import BeautifulSoup
import lxml
from testpage.models import Accounts
from datetime import datetime
from runapp.models import Fromproxy


def autorizen():
    isproxy = Fromproxy.objects.get(pk=1).proxy_val
    now = datetime.now()
    #param a дозапись
    f = open('runapp\logfile.txt', 'a')
    f.write('Function autorizen_rota: ' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\n')


    proxies = {
      'http': 'http://10.18.7.6:3128',
      'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = 'None'

    acount_list = Accounts.objects.all()
    for user in acount_list:
        user_name = user.name
        url = user.url_rota
        if url != 'None':
            headers = {
                'Content-Type': "text/xml",
                'Accept-Charset': "utf-8",
                'Cache-Control': "no-cache",
                }
            response = requests.get(url=url, headers=headers, proxies=proxies)

            #response = requests.post(url=url, data=payload, headers=headers)
            #print('Текст ответа: ', response.text)
            trace = BeautifulSoup(response.text, "lxml")
            result_block = trace.find('success')
            validate = result_block.get_text()
            if validate:
                api_key = trace.find('apikey').get_text()
                f.write(user_name + ': ' + validate + ': ' + api_key+ '\n')
                user.apikey_rota = api_key
                user.save()
            else:
                print(user_name + ': Error: ' + validate + ': ' + api_key)
                f.write(user_name + ': Error: ' + validate + ': ' + api_key)
    f.write('\n')
    f.close()
