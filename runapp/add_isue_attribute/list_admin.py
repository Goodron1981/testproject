from runapp.models import Keys_List
import xlrd
import re

def add_last_key(root, image_text, keyword, extraword, extraimage, extrakeyword):
    my_test = Keys_List.objects.filter(root_word=root)
    if my_test:
        print("Ключ '" + root + "' уже используется!")
        return False
    c = Keys_List.objects.count()
    if not extraword:
        extraword = extraimage = extrakeyword = 'None'
# добавить расчет длины ключа до запятой (если она есть) и потом это значение добавляется как параметр length_of_key
    keyvalue = root
    keylen = len(keyvalue)
    newkey = Keys_List(num = c+1, root_word = root, image_text = image_text, key_word = keyword, extra_word = extraword, extra_image_text = extraimage, extra_key_words = extrakeyword, length_of_key = keylen)
    newkey.save()
    key_list = Keys_List.objects.order_by('-length_of_key')
    number = 0
    for key in key_list:
        number = number + 1
        key.num = number
        key.save()
    print("Ключ '" + root + "' добавлен!")
    return True

def add_index_key(index, root, image_text, keyword, extraword, extraimage, extrakeyword):
    c = Keys_List.objects.count()
    flip = c
    while flip >= index:
        my_test = Keys_List.objects.get(num=flip)
        my_test.num = flip + 1
        my_test.save()
        flip = flip - 1
    if not extraword:
        extraword = extraimage = extrakeyword = 'None'

    newkey = Keys_List(num=index, root_word = root, image_text = image_text, key_word = keyword, extra_word = extraword, extra_image_text = extraimage, extra_key_words = extrakeyword)
    newkey.save()


def remoove_index_key(index):
    c = Keys_List.objects.count()
    flip = index+1
    my_test = Keys_List.objects.filter(num=index)
    if my_test:
        my_test.delete()
    while flip <= c:
        my_test = Keys_List.objects.get(num=flip)
        my_test.num = flip - 1
        my_test.save()
        flip = flip + 1


def get_index_key(index):
    my_test = Keys_List.objects.filter(num=index)
    return my_test

def set_index_key(index, root, image_text, keyword, extraword, extraimage, extrakeyword):
    my_test = Keys_List.objects.filter(num=index)
    if not extraword:
        extraword = extraimage = extrakeyword = 'None'

    newkey = my_test(root_word = root, image_text = image_text, key_word = keyword, extra_word = extraword, extra_image_text = extraimage, extra_key_words = extrakeyword)
    newkey.save()

def test():
    remoove_index_key(1)

#заливка ключей
def loaddta():
    workbook = xlrd.open_workbook('runapp/add_isue_attribute/Keys.xlsx')
    sheet = workbook.sheet_by_index(0)
    for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        add_last_key(cols[0], cols[2],cols[1],cols[3],cols[5],cols[4])

def sorter():
    key_list = Keys_List.objects.all()
    for key in key_list:
        root = key.root_word
        # keyvalue = re.search(r'\w+', root)
        # keylen = len(keyvalue.group(0))
        keylen = len(root)
        key.length_of_key = keylen
        key.save()

    key_list = Keys_List.objects.order_by('-length_of_key')
    number = 0
    for key in key_list:
        number = number + 1
        key.num = number
        key.save()