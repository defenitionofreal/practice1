from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    """ Company Model """
    title = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class CustomUser(AbstractUser):
    """ Custom User Model """
    patronymic = models.CharField(max_length=100, verbose_name='Отчество',
                                  blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания',
                                null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Сertificate(models.Model):
    """ Certificate model """
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания')
    id_certificate = models.CharField(max_length=250, unique=True,
                                      verbose_name='Сертификат')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return self.id_certificate

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Nonce(models.Model):
    """ Nonce model """
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания')
    guid = models.CharField(max_length=250, unique=True, verbose_name='Ключ')
    data = models.CharField(max_length=250, verbose_name='Данные')
    signed_nonce = models.BinaryField()
    nonce = models.BinaryField()
    is_signed = models.BooleanField(default=False, verbose_name='Подпись')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.guid

    class Meta:
        verbose_name = 'Нонс'
        verbose_name_plural = 'Нонсы'


class JwtToken(models.Model):
    """ JWT token model """
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания')
    token = models.CharField(max_length=1000, unique=True,
                             verbose_name='Токен')
    status = models.BooleanField(default=False, verbose_name='Статус')
    field = models.CharField(max_length=1000, verbose_name='Поле')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'
