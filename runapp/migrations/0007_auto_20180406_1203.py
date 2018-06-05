# Generated by Django 2.0.1 on 2018-04-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runapp', '0006_auto_20180404_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='GUrl_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href_url', models.CharField(default='None', max_length=200, verbose_name='URL страницы')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
        ),
        migrations.AlterField(
            model_name='isue',
            name='keywords_parse',
            field=models.TextField(default='None', verbose_name='Keywords'),
        ),
    ]