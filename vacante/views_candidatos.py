import pandas as pd
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Candidato, ConfiguracionCandidato
from .forms import CandidatoUploadForm


def cargar_candidatos(request):
    if request.method == "POST":
        form = CandidatoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES["archivo_excel"]
            df = pd.read_excel(archivo, header=None, skiprows=1)  # Leer sin encabezados para usar índices de columna

            # Obtener la configuración de columnas
            configuracion = ConfiguracionCandidato.objects.first()
            if not configuracion:
                return render(request, "cargar_candidatos.html", {
                    "form": form, 
                    "error": "No hay configuración de columnas definida."
                })

            # Procesar cada fila del archivo Excel
            for _, row in df.iterrows():
                try:
                    Candidato.objects.create(
                        id_vacante=row[configuracion.col_id_vacante],
                        identificacion=row[configuracion.col_identificacion],
                        nombre=row[configuracion.col_nombre],
                        es_interno=True if row[configuracion.col_es_interno] == "Sí" else False,
                        titulo=row[configuracion.col_titulo],
                        otro_titulo=row[configuracion.col_otro_titulo] if not pd.isna(row[configuracion.col_otro_titulo]) else None,
                        nivel_estudios=row[configuracion.col_nivel_estudios],
                        fecha_fin_estudios=str(row[configuracion.col_fecha_fin_estudios]) if not pd.isna(row[configuracion.col_fecha_fin_estudios]) else "",
                        fecha_diploma=str(row[configuracion.col_fecha_diploma]) if not pd.isna(row[configuracion.col_fecha_diploma]) else "",
                        cumple_requisitos=False,  # Se evaluará después
                        justificacion=""
                    )
                except KeyError as e:
                    return render(request, "cargar_candidatos.html", {
                        "form": form,
                        "error": f"Error al procesar el archivo: {str(e)}"
                    })

            return redirect("lista_candidatos")  # Redirigir a la lista después de cargar

    else:
        form = CandidatoUploadForm()

    return render(request, "cargar_candidatos.html", {"form": form})

def lista_candidatos(request):
    candidatos = Candidato.objects.all().order_by('titulo')
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

def limpiar_candidatos(request):
    Candidato.objects.all().delete()
    return redirect('lista_candidatos')
    
