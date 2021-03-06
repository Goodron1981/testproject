# Generated by Django 2.0.1 on 2018-04-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runapp', '0005_keys_list_key_words'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keys_list',
            old_name='key_words',
            new_name='key_word',
        ),
        migrations.RemoveField(
            model_name='keys_list',
            name='roots',
        ),
        migrations.AddField(
            model_name='keys_list',
            name='extra_image_text',
            field=models.CharField(default='None', max_length=100, verbose_name='Текст поиска вторичной картинки'),
        ),
        migrations.AddField(
            model_name='keys_list',
            name='extra_key_words',
            field=models.TextField(default='None', max_length=100, verbose_name='Вторичная ключевая фраза'),
        ),
        migrations.AddField(
            model_name='keys_list',
            name='extra_word',
            field=models.TextField(default='None', max_length=100, verbose_name='Вторичное слово'),
        ),
        migrations.AddField(
            model_name='keys_list',
            name='root_word',
            field=models.TextField(default='None', max_length=100, verbose_name='Корневое слово'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='anchor1_url',
            field=models.CharField(default='None', max_length=200, verbose_name='Ссылка анкора'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='blogun_isue_url',
            field=models.CharField(default='None', max_length=200, verbose_name='Урл заявки блогуна'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='check_url_rota',
            field=models.CharField(default='None', max_length=200, verbose_name='Урл решения рота'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='img_url',
            field=models.CharField(default='None', max_length=300, verbose_name='Урл картинки'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='title_parse',
            field=models.TextField(default='None', verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='keys_list',
            name='image_text',
            field=models.CharField(default='None', max_length=100, verbose_name='Текст поиска корневой картинки'),
        ),
    ]
