# Generated by Django 2.0.1 on 2018-03-06 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0008_auto_20180303_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='adddate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounts',
            name='auth_blog',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='token_sape',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='url_rota',
            field=models.URLField(default='None'),
        ),
    ]
