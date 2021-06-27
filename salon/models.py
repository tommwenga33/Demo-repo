from django.db import models


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='service')
    des = models.TextField()


class Price(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='price')
    price = models.IntegerField()


class Photos(models.Model):
    img = models.ImageField(upload_to='gallery')


class Style1(models.Model):
    img = models.ImageField(upload_to='style1')
