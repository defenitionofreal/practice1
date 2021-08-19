from django.db import models
from ..users.models import Company


class Product(models.Model):
    """ Product model """
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания')
    title = models.CharField(max_length=250, verbose_name='Название')
    code = models.CharField(max_length=250, unique=True,
                            verbose_name='Код честный знак')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class MarkingCode(models.Model):
    """ Marking code model """

    NEW = 'Новый'
    SENT = 'Отдан на печать'
    CONFIRMED = 'Распечатка подтверждена'
    DEPRECATED = 'Устарел до выдачи'
    LOST_BEFORE = 'Утрачен до печати'
    LOST_AFTER = 'Утрачен после печати'
    SCANNED = 'Отсканирован'
    SUCCESSFULL = 'Успешно введен в оборот'
    ERROR = 'Ошибка при вводе в оборот'

    STATUS_CHOICES = [
        (NEW, 'Новый'),
        (SENT, 'Отдан на печать'),
        (CONFIRMED, 'Распечатка подтверждена'),
        (DEPRECATED, 'Устарел до выдачи'),
        (LOST_BEFORE, 'Утрачен до печати'),
        (LOST_AFTER, 'Утрачен после печати'),
        (SCANNED, 'Отсканирован'),
        (SUCCESSFULL, 'Успешно введен в оборот'),
        (ERROR, 'Ошибка при вводе в оборот'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар')
    value = models.CharField(max_length=1000, verbose_name='Значение')
    status = models.CharField(choices=STATUS_CHOICES, max_length=100, verbose_name='Статус')
    timestamp_get = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Таймштамп получения')
    timestamp_circulation = models.DateTimeField(
        verbose_name='Таймштамп ввода в оборот')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Код Маркировки'
        verbose_name_plural = 'Коды Маркировок'
