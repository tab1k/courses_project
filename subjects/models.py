from django.db import models

from categories.models import *


# Create your models here.


class Teachers(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(blank=False)
    education = models.TextField(blank=True)
    salary = models.IntegerField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Subjects(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField(blank=True)
    course_time = models.CharField(max_length=100)
    price = models.IntegerField(blank=False)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

