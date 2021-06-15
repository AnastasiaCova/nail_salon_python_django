from django.contrib import admin
from .models import News, PriceList, Reviews, Order

admin.site.register(News)
admin.site.register(PriceList)
admin.site.register(Reviews)
admin.site.register(Order)

