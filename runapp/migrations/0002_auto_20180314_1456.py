# Generated by Django 2.0.1 on 2018-03-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='isue',
            name='ubdate_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='isue',
            name='id_campaign_blogun',
            field=models.IntegerField(verbose_name='ID кампании блогуна'),
        ),
        migrations.AlterField(
            model_name='isue',
            name='id_isue',
            field=models.IntegerField(verbose_name='ID заявки'),
        ),
    ]
