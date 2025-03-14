from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import CampoEspecificoPregrado
from .forms import BulkUploadCampoEspecificoForm, CampoEspecificoPregradoForm
import pandas as pd
from django.contrib import messages

def campo_especifico_list(request):
    campos = CampoEspecificoPregrado.objects.all().order_by('descripcion')
    return render(request, 'campo_especifico_list.html', {'campos': campos})

def campo_especifico_create(request):
    if request.method == 'POST':
        form = CampoEspecificoPregradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campo_especifico_list')
    else:
        form = CampoEspecificoPregradoForm()
    return render(request, 'campo_especifico_form.html', {'form': form})

@require_POST
def campo_especifico_delete(request, pk):
    campo = get_object_or_404(CampoEspecificoPregrado, pk=pk)
    campo.delete()
    CampoEspecificoPregrado.objects.all().delete()
    return redirect('campo_especifico_list')

def campo_especifico_bulk_upload(request):
    if request.method == 'POST':
        form = BulkUploadCampoEspecificoForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, f"Error al leer el archivo: {e}")
                return redirect('campo_especifico_bulk_upload')
            if df.shape[1] != 1:
                messages.error(request, "El archivo debe tener solo una columna con las descripciones.")
                return redirect('campo_especifico_bulk_upload')
            df = df.drop_duplicates()
            for index, row in df.iterrows():
                descripcion = str(row.iloc[0]).strip()
                if descripcion:
                    CampoEspecificoPregrado.objects.get_or_create(descripcion=descripcion)
            messages.success(request, "Carga masiva realizada correctamente.")
            return redirect('campo_especifico_list')
    else:
        form = BulkUploadCampoEspecificoForm()
    return render(request, 'campo_especifico_bulk_upload.html', {'form': form})
