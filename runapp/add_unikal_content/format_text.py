# Тут выполняется обрезка текста под переводчик и под уникальность.
import re
from runapp.models import Excludestate

def format_cut_content(textcont, lencont, serchurl):
    # 1. Номера телефонов
    # 2. Слова похожие на название сайта (более 3-х символов)
    butarr = re.findall('\w+', serchurl)

    word_list = Excludestate.objects.all()
    resulttext = ''
    maxlen = lencont * 1.2
    # 1 разбить на предложения
    arrspend = re.split(r'[.!?]\s*', textcont)
    # 2 проверить каждое предложение на наличие исключающих слов
    for peace in arrspend:
        for word in word_list:
            serchword = word.ex_state + '\w*\\b\s*'
            validresult = re.search(r'\b' + serchword, peace.lower())
    # 3 варифицированнные предложения склеиваем и подсчитываем чтобы были не меньше lencont и не больше maxlen
            if validresult:
                break
        else:
            for but in butarr:
                if len(but) > 3:
                    serchword = but + '\w*\\b\s*'
                    secondvalid = re.search(r'\b' + serchword, peace.lower())
                    if secondvalid:
                        break
            else: resulttext = resulttext + peace + '. '
        if len(resulttext) >= maxlen:
            break
    # 4 возвращаем варифицированый кусок
    # print(len(resulttext))
    finaltext = re.sub('\s*["«][А-ЯA-Z]\w+["»]', '', resulttext)
    return finaltext