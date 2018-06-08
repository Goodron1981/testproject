# Будет запускать вторую часть: подборка уникального текста и ее публикация
from runapp.models import Isue, GUrl_List
from runapp.add_unikal_content.search_url_google import geturls
from runapp.add_unikal_content.parse_page import getcontent
from runapp.add_unikal_content.format_text import format_cut_content
from runapp.add_unikal_content.translate import translatecont
from runapp.add_unikal_content.unikal_test import getunikal
from runapp.publication.public_content import publilconent
import re

def complete():
    isue_list = Isue.objects.filter(status_isue='AddKey')
    for isue in isue_list:
        key_isue = isue.key_words
        isue_type = isue.type_isue
        isue_num = isue.num
# Postovoi - 500-1000, Post(статья) -1000-1500, PressRelease - 2000-2500; link и archive = 1000, остальные = 2000
# Postovoi - 800, link и archive = 1000, остальные = 2000
        if isue_type == 'Postovoi':
            charlength = 600
        elif isue_type == 'link' or isue_type == 'archive':
            charlength = 1000
        else: charlength = 2000
        page = 2
        while page < 5:
            arrurls = geturls(key_isue, page)
            for gurl in arrurls:
                # Если найденый урл уже есть то его пропускаем, иначе записываем в список
                my_test = GUrl_List.objects.filter(href_url=gurl)
                if not my_test:
                    newurl = GUrl_List(href_url = gurl)
                    newurl.save()
                    firstcontent = getcontent(gurl)
                    if len(firstcontent) >= charlength:
                        secondcontent = format_cut_content(firstcontent,charlength,gurl)
                        validlength = re.findall(r'\S', secondcontent.lower())
                        if len(validlength) >= charlength:
                            firdcontent = translatecont(secondcontent)
                            unikalresult = getunikal(firdcontent)
                            if unikalresult > 70:
                                publikresult = publilconent(firdcontent, isue_num)
                                isue.public_url = publikresult
                                isue.public_content = firdcontent
                                isue.status_isue = "AddUnikal"
                                isue.save()
                                break
            if isue.public_url != 'None':
                break
            page += 1
        else: isue.public_content = "Текст не найден!"