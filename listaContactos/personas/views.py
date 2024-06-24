from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm, RawPersonaForm
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )

# Create your views here.
class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Persona.objects.filter(edad__lte='40')
        return JsonResponse(list(queryset.values()), safe = False)

class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador'
        ]

class PersonaCreateView(CreateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador'
        ]

class PersonaDetailView(DetailView):
    model = Persona
    
class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte='40')

def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto': obj,
        }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView1(request):
    initialValues = {
        'nombres': 'Sin Nombre'
        }
    form = PersonaForm(request.POST or None, initial = initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    context = {
        'form': form
        }
    return render(request, 'personas/personasCreate.html', context)

def personaCreateView2(request):
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})

def personasAnotherCreateView(request):
    form = RawPersonaForm() #request.GET
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form,
        }
    return render(request, 'personas/personasCreate.html', context)

def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    context = {
        'objeto': obj,
        }
    return render(request, 'personas/descripcion.html', context)

def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList': queryset,
        }
    return render(request, 'personas/personasLista.html', context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    if request.method == 'POST':
        print("lo borro")
        obj.delete()
        return redirect('../')
    context = {
        'objeto': obj,
        }
    return render(request, 'personas/personasBorrar.html', context)