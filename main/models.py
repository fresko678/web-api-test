from django.db import models
from datetime import date
from django.core.validators import RegexValidator


class Animal(models.Model):
    type = models.CharField('Тип животного', max_length=50)
    name = models.CharField('Кличка', max_length=50)
    birthday = models.DateField('Дата рождения')
    height = models.FloatField('Рост')
    weight = models.FloatField('Вес')
    passport = models.BooleanField('Наличие паспорта')
    pass_num = models.CharField('Номер паспорта', blank=True, null=True, max_length=50, validators=[RegexValidator('^[a-zA-Z0-9]+$')])

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'
