from django.contrib.auth.models import User
from django import forms
from main.models import Order, Reviews, PriceList
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput, Select, FileField
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget = forms.PasswordInput)
    

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('fullname', 'pricelist', 'phone', 'data')

        widgets = {
            'fullname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            'pricelist': Select(attrs={
                'class': 'form-control',
            'placeholder': 'Услуга'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
            'placeholder': 'Телефон'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время'
            }),
        }

class AddPriceForm(ModelForm):
    class Meta:
        model = PriceList
        fields = ('name', 'price', 'picture')

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
            'placeholder': 'Цена'
            }),
        }


class EditOrdForm(ModelForm):

    class Meta:
        model = Order
        fields = ('fullname', 'pricelist', 'phone', 'data')

        widgets = {
            'fullname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            'pricelist': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Услуга'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время'
            }),
        }


class EditPriceForm(ModelForm):

    class Meta:
        model = PriceList
        fields = ('name', 'price', 'picture')

    widgets = {
        'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название'
        }),
        'price': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Цена'
        }),
    }