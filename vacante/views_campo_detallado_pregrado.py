from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import CampoDetalladoPregrado
from .forms import CampoDetalladoPregradoForm
import pandas as pd
from .forms import BulkUploadDetalladoPregradoForm 

def campo_detallado_list(request):
    campos = CampoDetalladoPregrado.objects.all().order_by('descripcion')
    return render(request, 'campo_detallado_pregrado_list.html', {'campos': campos})

def campo_detallado_create(request):
    if request.method == 'POST':
        form = CampoDetalladoPregradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campo_detallado_pregrado_list')
    else:
        form = CampoDetalladoPregradoForm()
    return render(request, 'campo_detallado_pregrado_form.html', {'form': form})

@require_POST
def campo_detallado_delete(request, pk):
    campo = get_object_or_404(CampoDetalladoPregrado, pk=pk)
    campo.delete()
    return redirect('campo_detallado_pregrado_list')

def campo_detallado_bulk_upload(request):
    if request.method == 'POST':
        form = BulkUploadDetalladoPregradoForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, f"Error al leer el archivo: {e}")
                return redirect('campo_detallado_bulk_pregrado_upload')
            if df.shape[1] != 1:
                messages.error(request, "El archivo debe tener solo una columna con las descripciones.")
                return redirect('campo_detallado_bulk_pregrado_upload')
            df = df.drop_duplicates()
            for index, row in df.iterrows():
                descripcion = str(row.iloc[0]).strip()
                if descripcion:
                    CampoDetalladoPregrado.objects.get_or_create(descripcion=descripcion)
            messages.success(request, "Carga masiva realizada correctamente.")
            return redirect('campo_detallado_pregrado_list')
    else:
        form = BulkUploadDetalladoPregradoForm()
    return render(request, 'campo_detallado_bulk_pregrado_upload.html', {'form': form})
