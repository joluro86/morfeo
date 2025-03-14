from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import CampoAmplioPregrado
from .forms import CampoAmplioPregradoForm
import pandas as pd
from django.contrib import messages
from .forms import BulkUploadCampoAmplioForm

def campo_amplio_list(request):
    """Vista para listar todos los objetos de CampoAmplio."""
    campos = CampoAmplioPregrado.objects.all().order_by('descripcion')
    return render(request, 'campo_amplio_list.html', {'campos': campos})

def campo_amplio_create(request):
    """Vista para crear una nueva instancia de CampoAmplio."""
    if request.method == 'POST':
        form = CampoAmplioPregradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campo_amplio_list')
    else:
        form = CampoAmplioPregradoForm()
    return render(request, 'campo_amplio_form.html', {'form': form})

@require_POST
def campo_amplio_delete(request, pk):
    campo = get_object_or_404(CampoAmplioPregrado, pk=pk)
    campo.delete()
    return redirect('campo_amplio_list')


def campo_amplio_bulk_upload(request):
    if request.method == 'POST':
        form = BulkUploadCampoAmplioForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            try:
                # Leer el archivo Excel
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, f"Error al leer el archivo: {e}")
                return redirect('campo_amplio_bulk_upload')
            
            # Verificar que el archivo tenga una sola columna
            if df.shape[1] != 1:
                messages.error(request, "El archivo debe tener solo una columna con las descripciones.")
                return redirect('campo_amplio_bulk_upload')
            
            # Iterar sobre cada fila y crear el objeto si la descripción no está vacía
            for index, row in df.iterrows():
                descripcion = str(row.iloc[0]).strip()
                if descripcion:
                    # Evita duplicados usando get_or_create (considera que el campo ya es único en el modelo)
                    CampoAmplioPregrado.objects.get_or_create(descripcion=descripcion)
            
            messages.success(request, "Carga masiva realizada correctamente.")
            return redirect('campo_amplio_list')
    else:
        form = BulkUploadCampoAmplioForm()
    
    return render(request, 'campo_amplio_bulk_upload.html', {'form': form})
