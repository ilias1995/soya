# coding: utf-8
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Soyainfo(models.Model):
    soya_sort = models.CharField(max_length=200)
    info = models.TextField()
    image = models.ImageField(upload_to='soyaimage')


class Products(models.Model):
    soya_sort = models.CharField(max_length=200)
    sena = models.IntegerField()
    image = models.ImageField(upload_to='soyaimage')


class Zakaz(models.Model):
    name = models.CharField(max_length=200)
    SORT_CHOICES = (
        ('P', 'Первый сорт'),
        ('V', 'Второй сорт'),
        ('T', 'Третий сорт'),
    )
    number = models.IntegerField()
    soya_sort = models.CharField(max_length=200, choices=SORT_CHOICES)
    how_many = models.IntegerField()
