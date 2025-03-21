from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProgramaAcademicoSnies
from .forms import ProgramaAcademicoSniesForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProgramaAcademicoSnies
import pandas as pd


def cargar_programas_academicos_snies(request):
    if request.method == "POST":
        archivo = request.FILES.get("archivo_excel")

        if not archivo:
            messages.error(request, "Debe seleccionar un archivo Excel.")
            return redirect("cargar_programas_academicos_snies")

        try:
            # Leer sin encabezado y desde la fila 2 (ignorar encabezado)
            df = pd.read_excel(archivo, header=None, skiprows=1)

            # Reemplazar valores NaN por "" (cadena vacía)
            df = df.fillna("")

            for _, row in df.iterrows():
                datos = {
                    "nombre_del_programa": str(row[0]).strip(),
                    "titulo_otorgado": str(row[1]).strip(),
                    "cine_f_2013_ac_campo_amplio": str(row[2]).strip(),
                    "cine_f_2013_ac_campo_especifico": str(row[3]).strip(),
                    "cine_f_2013_ac_campo_detallado": str(row[4]).strip(),
                    "area_de_conocimiento": str(row[5]).strip(),
                    "nucleo_basico_del_conocimiento": str(row[6]).strip(),
                    "nivel_academico": str(row[7]).strip(),
                    "nivel_de_formacion": str(row[8]).strip(),
                }

                ProgramaAcademicoSnies.objects.create(**datos)                    

            messages.success(request, "Archivo cargado correctamente.")
            return redirect("lista_programas_academicos_snies")

        except Exception as e:
            messages.error(request, f"Error al procesar el archivo: {e}")
            return redirect("cargar_programas_academicos_snies")

    return render(request, "cargar_programas_snies.html")


def lista_programas_academicos_snies(request):
    programas = ProgramaAcademicoSnies.objects.all().order_by('nombre_del_programa')
    return render(request, "lista_programas_snies.html", {"programas": programas})


def exportar_programas_snies_excel(request):
    queryset = ProgramaAcademicoSnies.objects.all().values(
        "nombre_del_programa", "titulo_otorgado", "cine_f_2013_ac_campo_amplio",
        "cine_f_2013_ac_campo_especifico", "cine_f_2013_ac_campo_detallado",
        "area_de_conocimiento", "nucleo_basico_del_conocimiento",
        "nivel_academico", "nivel_de_formacion"
    )
    df = pd.DataFrame(queryset)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=programas_academicos.xlsx'
    df.to_excel(response, index=False)
    return response
