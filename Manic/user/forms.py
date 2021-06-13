from django.contrib.auth.models import User
from django import forms
from main.models import Order, Reviews, PriceList
from django.forms import ModelForm, Textarea, TextInput, DateInput, Select, DateField, FileField
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget = forms.PasswordInput)
    

class OrderForm(ModelForm):
    data = forms.CharField(label='Дата', widget = AdminDateWidget)

    class Meta:
        model = Order
        fields = ('fullname', 'pricelist', 'phone', 'data', 'time')

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
            'time': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Время'
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


class EditPriceForm(ModelForm):

    class Meta:
        model = PriceList
        fields = ('name', 'price', 'picture')