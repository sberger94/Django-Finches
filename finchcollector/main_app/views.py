from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Finch, Habitat
from .forms import SpottedForm
# Create your views here.

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


def home(request):
    return HttpResponse('<h1>Hello ya filthy bird</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    habitats_not_seen_in = Habitat.objects.exclude(id__in = finch.habitats.all().values_list('id'))
    spotted_form = SpottedForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'spotted_form': spotted_form,
        'habitats': habitats_not_seen_in
        })

def add_sighting(request, finch_id):
    form = SpottedForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_habitat(request, finch_id, habitat_id):
    Finch.objects.get(id=finch_id).habitats.add(habitat_id)
    return redirect('detail', finch_id=finch_id)



class HabitatList(ListView):
    model = Habitat

class HabitatDetail(DetailView):
    model = Habitat

class HabitatCreate(CreateView):
    model = Habitat
    fields = '__all__'

class HabitatUpdate(UpdateView):
    model = Habitat
    fields = '__all__'

class HabitatDelete(DeleteView):
    model = Habitat
    success_url = '/habitats/'