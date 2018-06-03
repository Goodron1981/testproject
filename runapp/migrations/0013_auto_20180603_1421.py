# Generated by Django 2.0.1 on 2018-06-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runapp', '0012_keys_list_length_of_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fromproxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_val', models.BooleanField(verbose_name='Использовать прокси')),
            ],
        ),
        migrations.AlterField(
            model_name='isue',
            name='anchor1',
            field=models.CharField(default='None', max_length=300, verbose_name='Анкор1'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='anchor1_text',
            field=models.CharField(default='None', max_length=100, verbose_name='Текст анкора'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='status_isue',
            field=models.CharField(choices=[('Reword', 'REWORD'), ('Closed', 'CLOSED'), ('AddUnikal', 'ADDUNIKAL'), ('AddKey', 'ADDKEY'), ('New', 'NEW')], default='New', max_length=100, verbose_name='Статус заявки'),
        ),
    ]
