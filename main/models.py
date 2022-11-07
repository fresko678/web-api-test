from django.db import models
from django.core.validators import RegexValidator


class Type(models.Model):
    type = models.CharField('Тип животного', max_length=50, validators=[RegexValidator('^[а-яА-Я]+$')])

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class Animal(models.Model):
    type = models.ForeignKey(Type, verbose_name="Тип животного", on_delete=models.CASCADE)
    name = models.CharField('Кличка', max_length=50, validators=[RegexValidator('^[а-яА-Я]+$')], )
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
