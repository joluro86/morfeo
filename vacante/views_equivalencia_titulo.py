import openpyxl
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EquivalenciaTitulo, NovedadEquivalencia
from django.views import View
from django.core.files.storage import default_storage


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
            EquivalenciaTitulo.objects.create(
                titulo=row[0],                 # Columna A
                otro_titulo=row[1],           # Columna B
                nivel_estudios=row[2],        # Columna C
                equivalente_snies=row[3]      # Columna D
            )

        messages.success(request, 'Datos cargados correctamente desde el Excel.')
        return redirect('lista_equivalencia_titulo')



class ListaEquivalenciaTitulo(View):
    def get(self, request):
        equivalencias = EquivalenciaTitulo.objects.all()
        return render(request, 'equivalencia_titulo_lista.html', {
            'equivalencias': equivalencias
        })
        
class ListaNovedades(View):
    def get(self, request):
        novedades = NovedadEquivalencia.objects.select_related('equivalencia', 'sugerencia_snies')
        return render(request, 'novedades_equivalencia_titulo.html', {'novedades': novedades})



class BuscarEquivalenciasView(View):
    def get(self, request):
        buscar_equivalencias_snies()
        messages.success(request, "Búsqueda de equivalencias completada.")
        return redirect('lista_equivalencia_titulo')

from .models import EquivalenciaTitulo, ProgramaAcademicoSnies, NovedadEquivalencia
from django.db.models import Q

from django.db.models import Q
from .models import EquivalenciaTitulo, ProgramaAcademicoSnies, NovedadEquivalencia

def buscar_equivalencias_snies():
    palabras_excluir = ['bachiller', 'completar', 'posgrado', 'postgrado']

    equivalencias = EquivalenciaTitulo.objects.filter(equivalente_snies__isnull=True)

    for eq in equivalencias:
        titulo = (eq.titulo or '').strip()
        otro_titulo = (eq.otro_titulo or '').strip()

        if not titulo and not otro_titulo:
            continue  # Si ambos están vacíos, no tiene sentido buscar

        texto = titulo.lower() + ' ' + otro_titulo.lower()
        if any(p in texto for p in palabras_excluir):
            continue

        # Armar consulta dinámica
        query = Q()
        if titulo:
            query |= Q(titulo_otorgado__icontains=titulo)
            query |= Q(nombre_del_programa__icontains=titulo)
        if otro_titulo:
            query |= Q(titulo_otorgado__icontains=otro_titulo)
            query |= Q(nombre_del_programa__icontains=otro_titulo)

        match = ProgramaAcademicoSnies.objects.filter(query).first()

        if match:
            eq.equivalente_snies = match.titulo_otorgado  # O puedes guardar el ID si haces FK
            eq.save()
        else:
            if not NovedadEquivalencia.objects.filter(equivalencia=eq).exists():
                NovedadEquivalencia.objects.create(
                    equivalencia=eq,
                    descripcion=f"No se encontró coincidencia para: '{eq.titulo or eq.otro_titulo}'"
                )

from django.shortcuts import get_object_or_404
from django.views import View
from django.forms import ModelChoiceField
from django import forms

class EditarNovedadesForm(forms.ModelForm):
    sugerencia_snies = forms.ModelChoiceField(
        queryset=ProgramaAcademicoSnies.objects.all(),
        required=False,
        label='Seleccionar título SNIES',
        widget=forms.Select(attrs={'class': 'w-full rounded border p-1'})
    )

    class Meta:
        model = NovedadEquivalencia
        fields = ['sugerencia_snies', 'revisado']

from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import EquivalenciaTitulo, NovedadEquivalencia, ProgramaAcademicoSnies
from .forms import EditarNovedadesForm

class EditarNovedadesEquivalencia(View):
    def get(self, request, pk):
        equivalencia = get_object_or_404(EquivalenciaTitulo, pk=pk)
        novedades = equivalencia.novedades.all()
        forms = [EditarNovedadesForm(instance=n, prefix=str(n.id)) for n in novedades]
        lista_snies = ProgramaAcademicoSnies.objects.only('titulo_otorgado')  # más ligero
        return render(request, 'editar_novedades_equivalencia_titulo.html', {
            'equivalencia': equivalencia,
            'forms': zip(novedades, forms),
            'lista_snies': lista_snies
        })

    def post(self, request, pk):
        equivalencia = get_object_or_404(EquivalenciaTitulo, pk=pk)
        novedades = equivalencia.novedades.all()
        for n in novedades:
            prefix = str(n.id)
            form = EditarNovedadesForm(request.POST, instance=n, prefix=prefix)
            if form.is_valid():
                texto_sugerido = request.POST.get(f'{prefix}-sugerencia_snies_text', '').strip()
                sugerido = ProgramaAcademicoSnies.objects.filter(titulo_otorgado=texto_sugerido).first()
                n.sugerencia_snies = sugerido
                n.revisado = form.cleaned_data['revisado']
                n.save()

                # Opcional: actualizar también el campo equivalente_snies del modelo principal
                if sugerido:
                    equivalencia.equivalente_snies = sugerido.titulo_otorgado
                    equivalencia.save()

        return redirect('lista_equivalencia_titulo')
