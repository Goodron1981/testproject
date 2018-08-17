from django.db import models
from django.contrib import admin

STATUS_CHOICES = (
    ("Reword", "REWORD"),
    ("Closed", "CLOSED"),
    ("AddUnikal", "ADDUNIKAL"),
    ("AddKey", "ADDKEY"),
    ("New", "NEW"),
)

# verbose_name='full name'
class Isue(models.Model):
    num = models.IntegerField(default = 1, verbose_name='№')
    id_isue = models.IntegerField(verbose_name='ID заявки')
    type_isue = models.CharField(max_length=10, default = 'None', verbose_name='Тип заявки')
    site_platform = models.CharField(max_length=40, default = 'None', verbose_name= 'Домен площадки')
    date_create = models.DateTimeField(verbose_name= 'Дата создания')
    anchor1 = models.CharField(max_length=300, default = 'None', verbose_name= 'Анкор1')
    anchor2 = models.CharField(max_length=100, default = 'None', verbose_name= 'Анкор2')
    anchor3 = models.CharField(max_length=100, default = 'None', verbose_name= 'Анкор3')
    anchor1_url = models.CharField(max_length=200, default = 'None', verbose_name= 'Ссылка анкора')
    anchor1_text = models.CharField(max_length=100, default = 'None', verbose_name= 'Текст анкора')
    check_url_rota = models.CharField(max_length=200, default = 'None', verbose_name= 'Урл решения рота')
    blogun_isue_url = models.CharField(max_length=200, default = 'None', verbose_name= 'Урл заявки блогуна')
    id_campaign_blogun = models.IntegerField(default = 0, verbose_name='ID кампании блогуна')
    title_parse = models.TextField(default = 'None', verbose_name= 'Title')
    keywords_parse = models.TextField(default = 'None', verbose_name= 'Keywords')
    key_words = models.CharField(max_length=100, default = 'None', verbose_name= 'Ключевая фраза')
    img_url = models.CharField(max_length=350, default = 'None', verbose_name= 'Урл картинки')
    user_platform = models.CharField(max_length=40, default = 'None', verbose_name= 'Пользователь')
    platform_name = models.CharField(max_length=40, default = 'None', verbose_name= 'Платформа')
    ubdate_date = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    public_content = models.TextField(default = 'None', verbose_name= 'Контент')
    public_url = models.CharField(max_length=200, default = 'None', verbose_name='Урл результата')
    status_isue = models.CharField(max_length=100, default = 'New', choices=STATUS_CHOICES, verbose_name='Статус заявки')
    # choices=STATUS_CHOICES

    def __str__(self):              # __unicode__ on Python 2
        return str(self.num)


class IsueAdmin(admin.ModelAdmin):

    list_display = ('num', 'id_isue', 'site_platform', 'user_platform', 'platform_name', 'public_url', 'ubdate_date', 'status_isue','key_words')
    '''
    list_display = (
    'num', 'id_isue', 'site_platform', 'user_platform', 'platform_name', 'public_url', 'ubdate_date', 'status_isue',
    'anchor1','title_parse','keywords_parse')
'''
    ordering = ('num',)
    actions = ['make_new']

    def make_new(self, request, queryset):
        queryset.update(status_isue='New',key_words = 'None',img_url = 'None')


    make_new.short_description = "Cler keyword and image"


class Keys_List(models.Model):
    num = models.IntegerField(default=1, verbose_name='№')
    root_word = models.TextField(max_length=100, default = 'None', verbose_name= 'Корневое слово')
    image_text = models.CharField(max_length=100, default = 'None', verbose_name= 'Текст поиска корневой картинки')
    key_word = models.TextField(max_length=100, default = 'None', verbose_name= 'Ключевая фраза')
    extra_word = models.TextField(max_length=100, default='None', verbose_name='Вторичное слово')
    extra_image_text = models.CharField(max_length=100, default='None', verbose_name='Текст поиска вторичной картинки')
    extra_key_words = models.TextField(max_length=100, default='None', verbose_name='Вторичная ключевая фраза')
    length_of_key = models.IntegerField(default=1, verbose_name='Длина ключа')

class Keys_ListAdmin(admin.ModelAdmin):
    list_display = ('num', 'root_word', 'image_text', 'key_word', 'extra_word', 'extra_image_text', 'extra_key_words', 'length_of_key')
    ordering = ('num',)
    search_fields = ('key_word', 'root_word')

class GUrl_List(models.Model):
    href_url = models.CharField(max_length=200, default = 'None', verbose_name= 'URL страницы')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

class GUrl_ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date')
    ordering = ('id',)

class Excludespage(models.Model):
    ex_page= models.CharField(max_length=100, default = 'None', verbose_name= 'Исключающие страницу')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

class ExcludespageAdmin(admin.ModelAdmin):
    list_display = ('ex_page', 'create_date')
    ordering = ('id',)

class Excludestate(models.Model):
    ex_state= models.CharField(max_length=100, default = 'None', verbose_name= 'Исключающие предложение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

class ExcludestateAdmin(admin.ModelAdmin):
    list_display = ('ex_state', 'create_date')
    ordering = ('id',)
    search_fields = ('ex_state',)

class Fromproxy(models.Model):
    proxy_val= models.BooleanField(verbose_name= 'Использовать прокси')


