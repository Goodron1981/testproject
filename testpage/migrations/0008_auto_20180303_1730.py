# Generated by Django 2.0.1 on 2018-03-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0007_auto_20180303_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='apikey_rota',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='auth_blog',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='cookies_sape',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='iduser_blog',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='name',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='token_sape',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='url_rota',
            field=models.CharField(default='None', max_length=40),
        ),
    ]
