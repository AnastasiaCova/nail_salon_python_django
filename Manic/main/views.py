from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from .models import News, PriceList, Reviews
from django.views.generic import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
# from django.contrib.auth.models import User
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


def Review(request):
    error = ''
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

# class PriceView(View):
#     def get(self, request, category):
#         prod = PriceList.objects.filter(category=category)
#         return render(request, 'main/product.html', {"prod": prod})
# #
#
# class ProductCardView(View):
#     def get(self, request, pk):
#         prod = Product.objects.filter(pk=pk)
#         return render(request, 'main/productcard.html', {"prod": prod})


def Sales(request):
    return render(request, 'main/sales.html')


# class NewsCard(View):
#     def get(self, request, pk):
#         news = MyNews.objects.filter(pk=pk)
#         return render(request, 'main/newscard.html', {"news": news})
#
#
# class BasketView(View):
#     def get(self, request):
#         prod = Basket.objects.all()
#         return render(request, 'main/basket.html', {"prod": prod})


# class submit(View):
#     def get(self, request, pk):
#         obj = Product.objects.get(pk=pk)
#         print(obj.numb, request.GET.get('numb'))
#         obj.name = request.GET.get('name')
#         obj.picture = request.GET.get('picture')
#         obj.price = request.GET.get('price')
#         obj.category = request.GET.get('category')
#         obj.numb = request.GET.get('numb')
#         obj.save()
#         return redirect('product/1')
#         return render(request, 'main/product.html')


# class AddToBasket(View):
#     def get(self, request, pk):
#         prod = Basket()
#         obj = Product.objects.get(pk=pk)
#         prod.product = obj
#         prod.product.numb = obj.numb
#         prod.save()
#         return redirect('/main/product/1')
#         return render(request, 'main/product.html')
#         return render(request, 'main/productcard.html')
#
#
# def delete(request, id):
#     obj = Basket.objects.get(id=id)
#     obj.delete()
#     return redirect('basket')
#     dict = {'basket': Basket.objects.all()}
#     return render(request, 'list/basket.html', context=dict)
#
#
# class News(ListView):
#     model = MyNews
#     paginate_by = 2
#     template_name = 'main/news.html'
#     context_object_name = 'mynews'
#     queryset = MyNews.objects.order_by('-data')
#
#     def get(self, request):
#         news = MyNews.objects.all()
#         return render(request, 'main/news.html', {"news": news})
#
#
# class AuthorBookList(ListView):
#     model = MyNews
#     template_name = 'main/author_book.html'
#
#     def get_queryset(self):
#         self.author_name = get_object_or_404(User, username = self.kwargs['author_name'])
#         return MyNews.objects.filter(user__username = self.author_name)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['author'] = self.author_name
#         return context


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