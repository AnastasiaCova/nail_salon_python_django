from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


class Time(models.Model):
    times = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.times.title()}'


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
    data = models.DateField(auto_now=False)
    time = models.ForeignKey(Time, related_name='time', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fullname.title()}'


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     phone = models.CharField(max_length=255, blank = True)
#
#     @receiver(post_save, sender = User)
#     def create_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user = instance)
#
#     @receiver(post_save, sender=User)
#     def save_profile(sender, instance, **kwargs):
#         try:
#             instance.profile.save()
#         except ObjectDoesNotExist:
#             Profile.objects.create(user=instance)
#
#     def __str__(self):
#         return f'{self.user}'
#
#
# class Order(models.Model):
#     TYPE = {
#         ('Наличными', 'Наличными'),
#         ('Картой курьеру', 'Картой курьеру'),
#         ('Картой на сайте', 'Картой на сайте')
#     }
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     pay = models.CharField(max_length=50, choices=TYPE, default="Картой на сайте")
#
#     def __str__(self):
#         return f'{self.name.title()}'
#
#
# class Basket(models.Model):
#     NUMB = {
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#         ('6', '6'),
#         ('7', '7')
#     }
#     #user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     numb = models.CharField(max_length=50, choices=NUMB, default="1")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.product.name.title()}'
