from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vacante, Candidato
from .forms import VacanteForm

def index(request):
    return render(request, 'index.html')

# Listar vacantes
class VacanteListView(ListView):
    model = Vacante
    template_name = 'vacante_list.html'
    context_object_name = 'vacantes'

# Crear vacante
class VacanteCreateView(CreateView):
    model = Vacante
    form_class = VacanteForm
    template_name = 'vacante_form.html'
    success_url = reverse_lazy('lista_vacantes')

# Editar vacante
class VacanteUpdateView(UpdateView):
    model = Vacante
    form_class = VacanteForm
    template_name = 'vacante_form.html'
    success_url = reverse_lazy('lista_vacantes')

# Eliminar vacante
class VacanteDeleteView(DeleteView):
    model = Vacante
    template_name = 'vacante_confirm_delete.html'
    success_url = reverse_lazy('lista_vacantes')
    
def limpiar(request):
    Vacante.objects.all().delete()
    print(len(Vacante.objects.all()))
    return redirect('campo_detallado_pregrado_list')
