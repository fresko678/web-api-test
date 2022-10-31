from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm
from django.views.generic import UpdateView, DeleteView
from .filters import AnimalFilter


def index(request):
    animals = Animal.objects.all()

    animal_filter = AnimalFilter(request.GET, queryset=animals)
    animals = animal_filter.qs

    data = {
        'animals': animals,
        'animal_filter': animal_filter
    }

    return render(request, 'main/index.html', data)


def add(request):
    error = ''

    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Неверное значение'

    form = AnimalForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add.html', data)


class Update(UpdateView):
    model = Animal
    template_name = 'main/add.html'
    form_class = AnimalForm


class Delete(DeleteView):
    model = Animal
    template_name = 'main/delete.html'
    success_url = '/'
