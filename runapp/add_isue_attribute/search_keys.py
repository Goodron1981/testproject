from runapp.models import Isue, Keys_List
import re
from .search_image import geturlimg

def add_keys_img():
    # isue_list = Isue.objects.all()
    isue_list = Isue.objects.filter(status_isue='New').order_by('num')
    keys_list = Keys_List.objects.order_by('num')
    for isue in isue_list:
        print("Поиск картинки",isue.num)
        if isue.key_words != "None":
            continue
        block1 = isue.anchor1
        block2 = isue.anchor2
        block3 = isue.anchor3
        block4 = isue.title_parse
        block5 = isue.keywords_parse
        all_data = ' ' + block1 + ' ' + block2 + ' ' + block3 + ' ' + block4 + ' ' + block5
        all_data = all_data.lower()
        for key in keys_list:
            repub = key.root_word.split(',')
            serchword = ''
            for word in repub:
                serchword = serchword + word + '\w*\\b\s*'
            result = re.search(r'\b' + serchword, all_data)
            if result:
                result2 = re.search(r'\b(' + serchword + '|' + key.extra_word + '\w*)\s*(' + key.extra_word + '\w*|' + serchword + ')', all_data)
                # result = re.search(r'\b(окна\w*|пластик\w*)\s*(пластик\w*|окна\w*)', str)
                if result2 and key.extra_key_words != 'None':
                    isue.key_words = key.extra_key_words
                    # Еще не верно так как должен быть еще поиск урла
                    isue.img_url = geturlimg(key.extra_image_text)
                    isue.status_isue = "AddKey"
                    isue.save()
                    break
                else:
                    isue.key_words = key.key_word
                    # Еще не верно так как должен быть еще поиск урла
                    isue.img_url = geturlimg(key.image_text)
                    isue.status_isue = "AddKey"
                    isue.save()
                    break