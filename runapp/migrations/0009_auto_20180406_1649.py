# Generated by Django 2.0.1 on 2018-04-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runapp', '0008_excludespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excludestate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_state', models.CharField(default='None', max_length=100, verbose_name='Исключающие предложение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
        ),
        migrations.RenameField(
            model_name='excludespage',
            old_name='ex_word',
            new_name='ex_page',
        ),
    ]
