from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from .views import Ord, Price
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    url(r'^login/$', views.Login, name='login'),
    path('ord', Ord.as_view(), name = 'ord'),
    path('price', Price.as_view(), name = 'price'),
    path('ordering', views.Ordering, name='ordering'),
    path('orderingdone', views.OrderingDone, name='orderingdone'),
    path('addprice', views.AddPrice, name='addprice'),
    path('addpricedone', views.AddPriceDone, name='addpricedone'),
    path('deleteord/<int:id>', views.DeleteOrd, name = 'deleteord'),
    path('editord/<int:id>', views.EditOrd, name = 'editord'),
    path('deleteprice/<int:id>', views.DeletePrice, name = 'deleteprice'),
    path('editprice/<int:id>', views.EditPrice, name = 'editprice'),

    path('jsi18n', JavaScriptCatalog.as_view(), name = 'js-catalog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)