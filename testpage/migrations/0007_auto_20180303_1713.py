# Generated by Django 2.0.1 on 2018-03-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0006_auto_20180303_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='apikey_rota',
            field=models.CharField(default='Apikey', max_length=20),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='auth_blog',
            field=models.CharField(default='Auth', max_length=20),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='cookies_sape',
            field=models.CharField(default='Cookies', max_length=20),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='iduser_blog',
            field=models.CharField(default='Iduser', max_length=20),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='name',
            field=models.CharField(default='Name', max_length=10),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='token_sape',
            field=models.CharField(default='Token', max_length=20),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='url_rota',
            field=models.CharField(default='Url', max_length=20),
        ),
    ]
