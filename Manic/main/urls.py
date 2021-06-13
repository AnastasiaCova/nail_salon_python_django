from django.contrib import admin
from django.urls import path
from . import views
from .views import Price, NewsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Main, name = 'main'),
    path('reviews', views.ReviewsView, name = 'reviews'),

    # path('product/<int:category>', ProductView.as_view(), name = 'product'),
    # path('productcard/<int:pk>', ProductCardView.as_view(), name = 'productcard'),

    path('sales', views.Sales, name = 'sales'),
    path('news', NewsView.as_view(), name = 'news'),
    path('portfolio', views.Portfolio, name = 'portfolio'),
    path('price', Price.as_view(), name = 'price'),

    path('order', views.Order, name = 'order'),
    path('orderdone', views.OrderDone, name = 'orderdone'),

    # path('newscard/<int:pk>', NewsCard.as_view()),
    # path('news/<author_name>', AuthorBookList.as_view()),
    #
    # path('basket', BasketView.as_view(), name = 'basket'),
    # # path('submit', views.submit, name = 'submit'),
    # path('addtobasket/<int:pk>', AddToBasket.as_view(), name = 'addtobasket'),
    # path('delete/<int:id>', views.delete, name = 'delete'),
    #
    # path('order', views.Order, name = 'order'),
    # path('orderdone', views.OrderDone, name = 'orderdone'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
