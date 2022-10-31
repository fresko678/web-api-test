from .models import Animal
from django.forms import ModelForm, TextInput, DateInput, NumberInput, CheckboxInput


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['type', 'name', 'birthday', 'height', 'weight', 'passport', 'pass_num']
        widgets = {
            "type": TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип животного'}),
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Кличка'}),
            "birthday": TextInput( attrs={'class': 'form-control', 'placeholder': 'Дата рождения', 'type': 'date'}),
            "height": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рост, см'}),
            "weight": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вес, кг'}),
            "passport": CheckboxInput(attrs={'type': 'checkbox', 'onclick': 'agreeForm(this.form)'}),
            "pass_num": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер паспорта', 'disabled': 'disabled', 'required': False})
        }
