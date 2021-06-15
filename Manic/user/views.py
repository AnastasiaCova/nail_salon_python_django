from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, OrderForm, AddPriceForm, EditOrdForm, EditPriceForm
from django.http import HttpResponseRedirect
from main.models import Order, PriceList
from django.views import View

class Ord(View):
    def get(self, request):
        prod = Order.objects.all()
        return render(request, 'user/ord.html', {"prod": prod})


class Price(View):
    def get(self, request):
        prod = PriceList.objects.all()
        return render(request, 'user/price.html', {"prod": prod})


def Ordering(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderingdone')
        else:
            error = 'Попробуйте еще раз'

    form = OrderForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'user/ordering.html', data)


def OrderingDone(request):
    return render(request, 'user/ordering_done.html')


def AddPrice(request):
    error = ''
    if request.method == 'POST':
        form = AddPriceForm(request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addpricedone')
        else:
            error = 'Попробуйте еще раз'

    data = {
        'form': AddPriceForm(),
        'error': error
    }

    return render(request, 'user/addprice.html', data)


def AddPriceDone(request):
    return render(request, 'user/addprice_done.html')


def Login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/user/ord')
                else:
                    error = 'Попробуйте еще раз'
            else:
                error = 'Попробуйте еще раз'
        error = 'Попробуйте еще раз'
    else:
        form = LoginForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'user/login.html', data)


def DeleteOrd(request, id):
    obj = Order.objects.get(id=id)
    obj.delete()
    return redirect('ord')
    dict = {
        'all': Order.objects.all()
    }
    return render(request, 'user/ord.html', context=dict)


def EditOrd(request, id):
    obj = Order.objects.get(id=id)
    if request.method == 'POST':
        form = EditOrdForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('ord')

    dict = {
        'obj': obj,
        'form': EditOrdForm(instance = obj),
    }
    return render(request, 'user/editord.html', context=dict)


def DeletePrice(request, id):
    obj = PriceList.objects.get(id=id)
    obj.delete()
    return redirect('price')
    dict = {
        'all': PriceList.objects.all()
    }
    return render(request, 'user/price.html', context=dict)


def EditPrice(request, id):
    obj = PriceList.objects.get(id=id)
    if request.method == 'POST':
        form = EditPriceForm(request.POST, files = request.FILES, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('price')

    dict = {
        'obj': obj,
        'form': EditPriceForm(instance=obj),
    }
    return render(request, 'user/editprice.html', context=dict)
