from main.models import Animal, Type
from django.forms import ModelForm, TextInput, DateInput, NumberInput, CheckboxInput, ModelChoiceField


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        type = ModelChoiceField(queryset=Type.objects.all(), empty_label=None, to_field_name="Тип животного")
        fields = ['type', 'name', 'birthday', 'height', 'weight', 'passport', 'pass_num']
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Кличка', 'pattern': '[а-яА-Я]+', 'title': 'Только буквы'}),
            "birthday": DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Дата рождения', 'type': 'date'}),
            "height": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рост, см'}),
            "weight": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вес, кг'}),
            "passport": CheckboxInput(attrs={'type': 'checkbox', 'onclick': 'agreeForm(this.form)'}),
            "pass_num": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер паспорта', 'disabled': 'disabled', 'required': False, 'pattern': '[a-zA-Z0-9]+', 'title': 'Неверный формат'})
        }
