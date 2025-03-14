import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import NivelAcademico
from .forms import NivelAcademicoForm, BulkUploadNivelAcademicoForm

def nivel_academico_list(request):
    niveles = NivelAcademico.objects.all().order_by('descripcion')
    return render(request, 'nivel_academico_list.html', {'niveles': niveles})

def nivel_academico_create(request):
    if request.method == 'POST':
        form = NivelAcademicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nivel_academico_list')
    else:
        form = NivelAcademicoForm()
    return render(request, 'nivel_academico_form.html', {'form': form})

@require_POST
def nivel_academico_delete(request, pk):
    nivel = get_object_or_404(NivelAcademico, pk=pk)
    nivel.delete()
    return redirect('nivel_academico_list')

def nivel_academico_bulk_upload(request):
    if request.method == 'POST':
        form = BulkUploadNivelAcademicoForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, f"Error al leer el archivo: {e}")
                return redirect('nivel_academico_bulk_upload')

            if df.shape[1] != 1:
                messages.error(request, "El archivo debe tener solo una columna con las descripciones.")
                return redirect('nivel_academico_bulk_upload')

            # Eliminar duplicados en el DataFrame para evitar procesar varias veces la misma descripción
            df = df.drop_duplicates()

            for index, row in df.iterrows():
                descripcion = str(row.iloc[0]).strip()
                if descripcion:
                    NivelAcademico.objects.get_or_create(descripcion=descripcion)

            messages.success(request, "Carga masiva realizada correctamente.")
            return redirect('nivel_academico_list')
    else:
        form = BulkUploadNivelAcademicoForm()
    return render(request, 'nivel_academico_bulk_upload.html', {'form': form})
