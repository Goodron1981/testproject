# Generated by Django 2.0.1 on 2018-04-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runapp', '0010_auto_20180411_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='isue',
            name='status_isue',
            field=models.CharField(default='New', max_length=100, verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='public_url',
            field=models.CharField(default='None', max_length=200, verbose_name='Урл результата'),
        ),
    ]
