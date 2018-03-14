from django.db import models
from django.contrib import admin

#verbose_name='full name'
class Isue(models.Model):
    num = models.IntegerField(default = 1, verbose_name='№')
    id_isue = models.IntegerField(verbose_name='ID заявки')
    type_isue = models.CharField(max_length=10, default = 'None', verbose_name='Тип заявки')
    site_platform = models.CharField(max_length=40, default = 'None', verbose_name= 'Домен площадки')
    date_create = models.DateTimeField(verbose_name= 'Дата создания')
    anchor1 = models.CharField(max_length=100, default = 'None', verbose_name= 'Анкор1')
    anchor2 = models.CharField(max_length=100, default = 'None', verbose_name= 'Анкор2')
    anchor3 = models.CharField(max_length=100, default = 'None', verbose_name= 'Анкор3')
    anchor1_url = models.URLField(max_length=200, default = 'None', verbose_name= 'Ссылка анкора')
    anchor1_text = models.CharField(max_length=40, default = 'None', verbose_name= 'Текст анкора')
    blogun_isue_url = models.URLField(max_length=200, default = 'None', verbose_name= 'Урл заявки блогуна')
    id_campaign_blogun = models.IntegerField(default = 0, verbose_name='ID кампании блогуна')
    check_url_blogun = models.URLField(max_length=200, default = 'None', verbose_name= 'Урл решения блогуна')
    title_parse = models.CharField(max_length=100, default = 'None', verbose_name= 'Title')
    keywords_parse = models.CharField(max_length=100, default = 'None', verbose_name= 'Keywords')
    key_words = models.CharField(max_length=100, default = 'None', verbose_name= 'Ключевая фраза')
    img_url = models.URLField(max_length=300, default = 'None', verbose_name= 'Урл картинки')
    user_platform = models.CharField(max_length=40, default = 'None', verbose_name= 'Пользователь')
    platform_name = models.CharField(max_length=40, default = 'None', verbose_name= 'Платформа')
    ubdate_date = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    def __str__(self):              # __unicode__ on Python 2
        return str(self.num)


class IsueAdmin(admin.ModelAdmin):
    list_display = ('num', 'site_platform', 'user_platform', 'platform_name','ubdate_date')
    ordering = ('num',)
