import pandas as pd
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Candidato
from .forms import CandidatoUploadForm

def cargar_candidatos(request):
    if request.method == "POST":
        form = CandidatoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo_excel']
            df = pd.read_excel(archivo)

            # Procesar cada fila del archivo Excel
            for _, row in df.iterrows():
                Candidato.objects.create(
                    id_vacante=row['id vacante'],
                    identificacion=row['Identificación del candidato'],
                    nombre=row['Nombre del Candidato'],
                    es_interno=True if row['¿Candidato es Interno?'] == 'Sí' else False,
                    titulo=row['Titulo Candidato'],
                    otro_titulo=row.get('Otro Título', None),
                    nivel_estudios=row['Nivel de estudios'],
                    fecha_fin_estudios=pd.to_datetime(row['Fecha fin de estudios'], errors='coerce').date(),
                    fecha_diploma=pd.to_datetime(row['Fecha de diploma'], errors='coerce').date(),
                    cumple_requisitos=False,  # Se evaluará después
                    justificacion=""
                )
            return redirect('lista_candidatos')  # Redirigir a la lista después de cargar

    else:
        form = CandidatoUploadForm()

    return render(request, "cargar_candidatos.html", {"form": form})

def lista_candidatos(request):
    candidatos = Candidato.objects.all().order_by('-id_vacante')
    paginator = Paginator(candidatos, 20)  # Mostramos 20 registros por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "lista_candidatos.html", {"page_obj": page_obj})
def exportar_candidatos_excel(request):
    candidatos = Candidato.objects.all().values()
    df = pd.DataFrame(candidatos)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="candidatos.xlsx"'
    df.to_excel(response, index=False)
    return response
