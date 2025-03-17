from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
import pandas as pd
from .models import CampoAmplioPosgrado
from .forms import CampoAmplioPosgradoForm, BulkUploadCampoAmplioPosgradoForm

def campo_amplio_posgrado_list(request):
    """Vista para listar todos los objetos de CampoAmplioPosgrado."""
    campos = CampoAmplioPosgrado.objects.all().order_by('descripcion')
    return render(request, 'campo_amplio_posgrado_list.html', {'campos': campos})

def campo_amplio_posgrado_create(request):
    """Vista para crear una nueva instancia de CampoAmplioPosgrado."""
    if request.method == 'POST':
        form = CampoAmplioPosgradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campo_amplio_posgrado_list')
    else:
        form = CampoAmplioPosgradoForm()
    return render(request, 'campo_amplio_posgrado_form.html', {'form': form})

@require_POST
def campo_amplio_posgrado_delete(request, pk):
    """Vista para eliminar una instancia de CampoAmplioPosgrado."""
    campo = get_object_or_404(CampoAmplioPosgrado, pk=pk)
    campo.delete()
    return redirect('campo_amplio_posgrado_list')

def campo_amplio_posgrado_bulk_upload(request):
    """Vista para la carga masiva de CampoAmplioPosgrado."""
    if request.method == 'POST':
        form = BulkUploadCampoAmplioPosgradoForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, f"Error al leer el archivo: {e}")
                return redirect('campo_amplio_posgrado_bulk_upload')
            
            if df.shape[1] != 1:
                messages.error(request, "El archivo debe tener solo una columna con las descripciones.")
                return redirect('campo_amplio_posgrado_bulk_upload')
            
            for index, row in df.iterrows():
                descripcion = str(row.iloc[0]).strip()
                if descripcion:
                    CampoAmplioPosgrado.objects.get_or_create(descripcion=descripcion)
            
            messages.success(request, "Carga masiva realizada correctamente.")
            return redirect('campo_amplio_posgrado_list')
    else:
        form = BulkUploadCampoAmplioPosgradoForm()
    
    return render(request, 'campo_amplio_posgrado_bulk_upload.html', {'form': form})
