from main.models import Animal
from main.forms import AnimalForm
from django.views.generic import UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from main.filters import AnimalFilter


class List(FilterView):
    model = Animal
    template_name = 'main/index.html'
    filterset_class = AnimalFilter


class Create(CreateView):
    model = Animal
    template_name = 'main/add.html'
    form_class = AnimalForm


class Update(UpdateView):
    model = Animal
    template_name = 'main/add.html'
    form_class = AnimalForm


class Delete(DeleteView):
    model = Animal
    template_name = 'main/delete.html'
    success_url = '/'
