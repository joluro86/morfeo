import openpyxl
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Candidato, EquivalenciaTitulo, NovedadEquivalencia
from django.views import View
from django.core.files.storage import default_storage
from .models import EquivalenciaTitulo, ProgramaAcademicoSnies, NovedadEquivalencia
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import View
from django.db.models import Q
from .models import EquivalenciaTitulo, ProgramaAcademicoSnies, NovedadEquivalencia
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import EquivalenciaTitulo, NovedadEquivalencia, ProgramaAcademicoSnies
from .forms import EditarNovedadesForm

class CargarExcelEquivalenciaTitulo(View):
    def get(self, request):
        return render(request, 'equivalencia_titulo_cargar_excel.html')

    def post(self, request):
        excel = request.FILES.get('excel_file')
        if not excel:
            messages.error(request, 'Debes subir un archivo Excel.')
            return redirect('cargar_equivalencia_titulo')

        # Guardar temporalmente y abrir con openpyxl
        path = default_storage.save('tmp/' + excel.name, excel)
        wb = openpyxl.load_workbook(default_storage.path(path))
        ws = wb.active

        # Recorrer desde la segunda fila (sin encabezado)
        for row in ws.iter_rows(min_row=2, values_only=True):
            if EquivalenciaTitulo.objects.filter(titulo=row[2]) or EquivalenciaTitulo.objects.filter(otro_titulo=row[3]):
                continue
               
            EquivalenciaTitulo.objects.create(
                id_vacante=row[0],            # Columna A
                id_candidato=row[1],          # Columna B
                titulo=row[2],                # Columna C
                otro_titulo=row[3],           # Columna D
                nivel_estudios=row[4],        # Columna E
                equivalente_snies=row[5]      # Columna F
            )
            

        messages.success(request, 'Datos cargados correctamente desde el Excel.')
        return redirect('lista_equivalencia_titulo')



class ListaEquivalenciaTitulo(View):
    def get(self, request):
        #EquivalenciaTitulo.objects.all().delete()
        equivalencias = EquivalenciaTitulo.objects.all()
        return render(request, 'equivalencia_titulo_lista.html', {
            'equivalencias': equivalencias
        })
        
class ListaNovedades(View):
    def get(self, request):
        #NovedadEquivalencia.objects.all().delete()
        novedades = NovedadEquivalencia.objects.filter(descripcion="Sin titulo equivalente")
        return render(request, 'novedades_equivalencia_titulo.html', {'novedades': novedades})


class BuscarEquivalenciasView(View):
    def get(self, request):
        buscar_equivalencias_snies()
        messages.success(request, "Búsqueda de equivalencias completada.")
        return redirect('lista_equivalencia_titulo')

def buscar_equivalencias_snies():
    equivalencias = EquivalenciaTitulo.objects.all()
    cont1 = 1
    
    for eq in equivalencias:
        if eq.nivel_estudios=="Bachiller" or eq.nivel_estudios=="bachiller" or eq.nivel_estudios=="Completar" or eq.nivel_estudios=="completar":
            eq.equivalente_snies= "No aplica"
            eq.save()
            continue
        
        if eq.titulo is not None:
            pro1 = ProgramaAcademicoSnies.objects.filter(titulo_otorgado=eq.titulo).first()
            if pro1 is None:
                pro2= ProgramaAcademicoSnies.objects.filter(nombre_del_programa=eq.titulo).first()
            if pro1 is not None:              
                eq.equivalente_snies=pro1.titulo_otorgado
                eq.save()
            elif pro2 is not None:
                eq.equivalente_snies=pro2.nombre_del_programa
                eq.save()
            
            else: 
                # Aquí creamos la NovedadEquivalencia si no se encontró coincidencia en SNIES
                NovedadEquivalencia.objects.create(
                    descripcion="Sin titulo equivalente",
                    id_vacante=eq.id_vacante,
                    identificacion_candidato=eq.id_candidato,
                    titulo=eq.titulo,
                    otro_titulo=eq.otro_titulo,
                    id_equivalencia=eq.id,
                )
                print(cont1)
                cont1 += 1 
             
        
class EditarNovedadesEquivalencia(View):
    def get(self, request, pk):
        equivalencia = get_object_or_404(EquivalenciaTitulo, pk=pk)
        lista_snies = ProgramaAcademicoSnies.objects.only('titulo_otorgado')  # más ligero
        return render(request, 'editar_novedades_equivalencia_titulo.html', {
            'equivalencia': equivalencia,
            'lista_snies': lista_snies
        })

    def post(self, request, pk):
        equivalencia = get_object_or_404(EquivalenciaTitulo, pk=pk)
        # Extraemos el dato enviado desde el input
        texto_sugerido = request.POST.get('nuevo_titulo_equivalente', '').strip()
        print("Texto sugerido:", texto_sugerido)
        # Buscamos en ProgramaAcademicoSnies un registro cuyo titulo_otorgado coincida con lo ingresado
        sugerido = ProgramaAcademicoSnies.objects.filter(titulo_otorgado=texto_sugerido).first()
        if sugerido:
            equivalencia.equivalente_snies = sugerido.titulo_otorgado
        else:
            equivalencia.equivalente_snies = texto_sugerido  # Se asigna el valor ingresado si no se encuentra en SNIES
        equivalencia.save()

        # Actualizamos la novedad asociada para quitar la marca de "Sin titulo equivalente"
        novedad = NovedadEquivalencia.objects.filter(id_equivalencia=equivalencia.id).first()
        if novedad:
            if novedad.descripcion == "Sin titulo equivalente":
                novedad.descripcion = equivalencia.equivalente_snies
                novedad.save()

        messages.success(request, "Equivalencia actualizada correctamente.")
        return redirect('lista_equivalencia_titulo')

