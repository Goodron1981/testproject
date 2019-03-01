from runapp.models import Isue
import openpyxl

def save_result():
    closed_isue_list = Isue.objects.filter(status_isue='Closed').order_by("num")
        # exclude(public_url = 'errorpublic')
    wb = openpyxl.load_workbook('/home/max/Рабочий стол/ForProjects/myvirtual/workproject/testproject/Обработка.xlsx')
    sheet = wb['Решено']
    last_row = len(sheet['A:A'])
    sheet.delete_rows(2, last_row-1)
   # wb.save('/home/max/Рабочий стол/ForProjects/myvirtual/workproject/testproject/Обработка.xlsx')
    my_count = 2
    for cisuie in closed_isue_list:
        sheet['A' + str(my_count)] = cisuie.num
        sheet['B' + str(my_count)] = cisuie.id_isue
        sheet['C' + str(my_count)] = cisuie.site_platform
        sheet['D' + str(my_count)] = cisuie.user_platform
        sheet['E' + str(my_count)] = cisuie.platform_name
        sheet['F' + str(my_count)] = cisuie.public_url
        sheet['G' + str(my_count)] = cisuie.ubdate_date
        sheet['H' + str(my_count)] = cisuie.status_isue
        sheet['I' + str(my_count)] = cisuie.key_words
        my_count = my_count + 1

    unclosed_isue_list = Isue.objects.exclude(status_isue='Closed').order_by("num")
    sheet2 = wb['Нерешено']
    last_row = len(sheet2['A:A'])
    sheet2.delete_rows(2, last_row - 1)
    my_count = 2
    for ucisuie in unclosed_isue_list:
        sheet2['A' + str(my_count)] = ucisuie.num
        sheet2['B' + str(my_count)] = ucisuie.id_isue
        sheet2['C' + str(my_count)] = ucisuie.site_platform
        sheet2['D' + str(my_count)] = ucisuie.user_platform
        sheet2['E' + str(my_count)] = ucisuie.platform_name
        sheet2['F' + str(my_count)] = ucisuie.public_url
        sheet2['G' + str(my_count)] = ucisuie.ubdate_date
        sheet2['H' + str(my_count)] = ucisuie.status_isue
        sheet2['I' + str(my_count)] = ucisuie.key_words
        my_count = my_count + 1
    wb.save('/home/max/Рабочий стол/ForProjects/myvirtual/workproject/testproject/Обработка.xlsx')