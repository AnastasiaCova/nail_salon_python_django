from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from .models import News, PriceList, Reviews
from django.views.generic import ListView
from .forms import OrderForm, ReviewForm


def Main(request):
    return render(request, 'main/main.html')


def ReviewsView(request):
        error = ''
        prod = Reviews.objects.all()
        if request.method == 'POST':
            form = ReviewForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('reviews')
            else:
                error = 'Попробуйте еще раз'

        form = ReviewForm()

        data = {
            'form': form,
            'error': error,
            "prod": prod
        }

        return render(request, 'main/reviews.html', data)


class NewsView(View):
    def get(self, request):
        prod = News.objects.all()
        return render(request, 'main/news.html', {"prod": prod})


def Portfolio(request):
    return render(request, 'main/portfolio.html')


class Price(View):
    def get(self, request):
        prod = PriceList.objects.all()
        return render(request, 'main/price.html', {"prod": prod})


def Sales(request):
    return render(request, 'main/sales.html')


def Order(request):
    error = ''
    print(request.method)
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('orderdone')
        else:
            error = 'Попробуйте еще раз'

    form = OrderForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/order.html', data)


def OrderDone(request):
    return render(request, 'main/order_done.html')