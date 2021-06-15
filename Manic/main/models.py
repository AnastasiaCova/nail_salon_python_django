from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


class PriceList(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/main')

    def __str__(self):
        return f'{self.name.title()}'


class News(models.Model):
    new = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/main')
    text = models.TextField()
    data = models.DateTimeField(auto_now=True, blank = True)

    def __str__(self):
        return f'{self.new.title()}'


class Reviews(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pricelist = models.ForeignKey(PriceList, related_name='reviewpricelist', on_delete=models.CASCADE, default="1")
    text = models.TextField()
    phone = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name.title()}'


class Order(models.Model):
    fullname = models.CharField(max_length=50)
    pricelist = models.ForeignKey(PriceList, related_name='orderpricelist', on_delete=models.CASCADE, default="1")
    phone = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f'{self.fullname.title()}'


