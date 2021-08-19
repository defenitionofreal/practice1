# Generated by Django 3.2.6 on 2021-08-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarkingCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000, verbose_name='Значение')),
                ('status', models.CharField(choices=[('Новый', 'Новый'), ('Отдан на печать', 'Отдан на печать'), ('Распечатка подтверждена', 'Распечатка подтверждена'), ('Устарел до выдачи', 'Устарел до выдачи'), ('Утрачен до печати', 'Утрачен до печати'), ('Утрачен после печати', 'Утрачен после печати'), ('Отсканирован', 'Отсканирован'), ('Успешно введен в оборот', 'Успешно введен в оборот'), ('Ошибка при вводе в оборот', 'Ошибка при вводе в оборот')], max_length=100, verbose_name='Статус')),
                ('timestamp_get', models.DateTimeField(auto_now_add=True, verbose_name='Таймштамп получения')),
                ('timestamp_circulation', models.DateTimeField(verbose_name='Таймштамп ввода в оборот')),
            ],
            options={
                'verbose_name': 'Код Маркировки',
                'verbose_name_plural': 'Коды Маркировок',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('code', models.CharField(max_length=250, unique=True, verbose_name='Код честный знак')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
