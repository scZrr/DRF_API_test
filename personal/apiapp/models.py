from django.db import models

class TopManager(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    state = models.CharField(max_length=255, verbose_name='Должность')
    start_date = models.DateField(verbose_name='Дата приема')
    salary = models.IntegerField(verbose_name='Зарплата')

    def __str__(self):
        return self.full_name


class Manager(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    state = models.CharField(max_length=255, verbose_name='Должность')
    start_date = models.DateField(verbose_name='Дата приема')
    salary = models.IntegerField(verbose_name='Зарплата')
    chef = models.ForeignKey(TopManager, on_delete=models.PROTECT, null=True, verbose_name='Начальник')

    def __str__(self):
        return self.full_name


class Engineer(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    state = models.CharField(max_length=255, verbose_name='Должность')
    start_date = models.DateField(verbose_name='Дата приема')
    salary = models.IntegerField(verbose_name='Зарплата')
    chef = models.ForeignKey(Manager, on_delete=models.PROTECT, null=True, verbose_name='Начальник')

    def __str__(self):
        return self.full_name