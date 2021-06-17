from django.contrib import admin
from django.urls import path
from . import views
from .views import Price, NewsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Main, name = 'main'),
    path('reviews', views.ReviewsView, name = 'reviews'),
    path('sales', views.Sales, name = 'sales'),
    path('news', NewsView.as_view(), name = 'news'),
    path('portfolio', views.Portfolio, name = 'portfolio'),
    path('price', Price.as_view(), name = 'price'),
    path('order', views.Order, name = 'order'),
    path('orderdone', views.OrderDone, name = 'orderdone'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
