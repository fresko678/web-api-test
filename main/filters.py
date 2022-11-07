import django_filters
from django_filters import NumberFilter
from main.models import Animal


class AnimalFilter(django_filters.FilterSet):
    weight_from = NumberFilter(field_name="weight", lookup_expr="gte")
    weight_to = NumberFilter(field_name="weight", lookup_expr="lte")

    class Meta:
        model = Animal
        fields = ['type', 'passport']
