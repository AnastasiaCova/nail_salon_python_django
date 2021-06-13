from .models import Order, Reviews
from django.forms import ModelForm, Textarea, TextInput, DateInput, Select, DateField


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
            'data': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })
        }


class ReviewForm(ModelForm):

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'pricelist', 'phone', 'text')

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            'pricelist': Select(attrs={
                'class': 'form-control',
            'placeholder': 'Услуга'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
            'placeholder': 'Телефон'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            })
        }