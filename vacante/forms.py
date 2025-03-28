from django import forms
from .models import NovedadEquivalencia, Vacante, EquivalenciaTitulo, CampoAmplioPregrado, CampoEspecificoPregrado, NivelAcademico, CampoDetalladoPregrado

class CampoAmplioPregradoForm(forms.ModelForm):
    class Meta:
        model = CampoAmplioPregrado
        fields = ['descripcion']
        
        labels = {
            'descripcion': 'Descripción',
        }
        error_messages = {
            'descripcion': {
                'required': 'Este campo es obligatorio.',
            }
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].required = True


class CampoEspecificoPregradoForm(forms.ModelForm):
    class Meta:
        model = CampoEspecificoPregrado
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción',
        }
        error_messages = {
            'descripcion': {
                'unique': 'Ya existe un Campo Especifico con esta descripción.',
                'required': 'Este campo es obligatorio.',
            },
        }


class BulkUploadCampoAmplioForm(forms.Form):
    excel_file = forms.FileField(
        label="Archivo Excel",
        help_text="Seleccione un archivo Excel (.xlsx) con una sola columna de descripciones."
    )
    
class BulkUploadCampoEspecificoForm(forms.Form):
    excel_file = forms.FileField(
        label="Archivo Excel",
        help_text="Seleccione un archivo Excel (.xlsx) con una sola columna de descripciones."
    )



class NivelAcademicoForm(forms.ModelForm):
    class Meta:
        model = NivelAcademico
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción',
        }
        error_messages = {
            'descripcion': {
                'unique': 'Ya existe un Nivel Académico con esta descripción.',
                'required': 'Este campo es obligatorio.',
            },
        }

class BulkUploadNivelAcademicoForm(forms.Form):
    excel_file = forms.FileField(
        label="Archivo Excel",
        help_text="Seleccione un archivo Excel (.xlsx) con una sola columna de descripciones."
    )


class CampoDetalladoPregradoForm(forms.ModelForm):
    class Meta:
        model = CampoDetalladoPregrado
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción',
        }
        error_messages = {
            'descripcion': {
                'unique': 'Ya existe un Campo Detallado con esta descripción.',
                'required': 'Este campo es obligatorio.',
            },
        }

class BulkUploadDetalladoPregradoForm(forms.Form):
    excel_file = forms.FileField(
        label="Archivo Excel",
        help_text="Seleccione un archivo Excel (.xlsx) con una sola columna de descripciones."
    )
    
    
from django import forms
from .models import CampoAmplioPosgrado

class CampoAmplioPosgradoForm(forms.ModelForm):
    class Meta:
        model = CampoAmplioPosgrado
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción',
        }
        error_messages = {
            'descripcion': {
                'unique': 'Ya existe un Campo Amplio con esta descripción.',
                'required': 'Este campo es obligatorio.',
            },
        }

from django import forms
from .models import CampoEspecificoPosgrado

class CampoEspecificoPosgradoForm(forms.ModelForm):
    class Meta:
        model = CampoEspecificoPosgrado
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción',
        }
        error_messages = {
            'descripcion': {
                'unique': 'Ya existe un Campo Específico con esta descripción.',
                'required': 'Este campo es obligatorio.',
            },
        }


from .models import CampoDetalladoPosgrado

class CampoDetalladoPosgradoForm(forms.ModelForm):
    class Meta:
        model = CampoDetalladoPosgrado
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción',
        }
        error_messages = {
            'descripcion': {
                'unique': 'Ya existe un Campo Detallado con esta descripción.',
                'required': 'Este campo es obligatorio.',
            },
        }

class BulkUploadCampoAmplioPosgradoForm(forms.Form):
    excel_file = forms.FileField(
        label="Archivo Excel",
        help_text="Seleccione un archivo Excel (.xlsx) con una sola columna de descripciones."
    )

class BulkUploadCampoEspecificoPosgradoForm(forms.Form):
    excel_file = forms.FileField(
        label="Archivo Excel",
        help_text="Seleccione un archivo Excel (.xlsx) con una sola columna de descripciones."
    )
class BulkUploadCampoDetalladoPosgradoForm(forms.Form):
    excel_file = forms.FileField(
        label="Archivo Excel",
        help_text="Seleccione un archivo Excel (.xlsx) con una sola columna de descripciones."
    )
    

from .models import Vacante

class VacanteForm(forms.ModelForm):
    class Meta:
        model = Vacante
        fields = ['numero', 'nivel_academico']
        labels = {
            'numero': 'Número de Vacante',
            'nivel_academico': 'Nivel Académico'
        }
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número único'}),
            'nivel_academico': forms.Select(attrs={'class': 'form-control'}),
        }


class CandidatoUploadForm(forms.Form):
    archivo_excel = forms.FileField(label="Subir archivo Excel", help_text="Seleccione un archivo con la lista de candidatos.")


from django import forms
from .models import ConfiguracionCandidato

class ConfiguracionCandidatoForm(forms.ModelForm):
    class Meta:
        model = ConfiguracionCandidato
        fields = [
            "nombre",
            "col_id_vacante",
            "col_identificacion",
            "col_nombre",
            "col_es_interno",
            "col_titulo",
            "col_otro_titulo",
            "col_nivel_estudios",
            "col_fecha_fin_estudios",
            "col_fecha_diploma",
        ]
        labels = {
            "nombre": "Nombre de la configuración",
            "col_id_vacante": "Columna de ID Vacante",
            "col_identificacion": "Columna de Identificación",
            "col_nombre": "Columna de Nombre",
            "col_es_interno": "Columna de Candidato Interno",
            "col_titulo": "Columna de Título",
            "col_otro_titulo": "Columna de Otro Título",
            "col_nivel_estudios": "Columna de Nivel de Estudios",
            "col_fecha_fin_estudios": "Columna de Fecha Fin de Estudios",
            "col_fecha_diploma": "Columna de Fecha de Diploma",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "col_id_vacante": forms.NumberInput(attrs={"class": "form-control"}),
            "col_identificacion": forms.NumberInput(attrs={"class": "form-control"}),
            "col_nombre": forms.NumberInput(attrs={"class": "form-control"}),
            "col_es_interno": forms.NumberInput(attrs={"class": "form-control"}),
            "col_titulo": forms.NumberInput(attrs={"class": "form-control"}),
            "col_otro_titulo": forms.NumberInput(attrs={"class": "form-control"}),
            "col_nivel_estudios": forms.NumberInput(attrs={"class": "form-control"}),
            "col_fecha_fin_estudios": forms.NumberInput(attrs={"class": "form-control"}),
            "col_fecha_diploma": forms.NumberInput(attrs={"class": "form-control"}),
        }

from django import forms
from .models import ProgramaAcademicoSnies

class ProgramaAcademicoSniesForm(forms.ModelForm):
    class Meta:
        model = ProgramaAcademicoSnies
        fields = "__all__"  # Incluir todos los campos

        widgets = {
            "nombre_del_programa": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "titulo_otorgado": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "cine_f_2013_ac_campo_amplio": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "cine_f_2013_ac_campo_especifico": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "cine_f_2013_ac_campo_detallado": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "area_de_conocimiento": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "nucleo_basico_del_conocimiento": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "nivel_academico": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
            "nivel_de_formacion": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded"}),
        }

        labels = {
            "nombre_del_programa": "Nombre del Programa",
            "titulo_otorgado": "Título Otorgado",
            "cine_f_2013_ac_campo_amplio": "Campo Amplio (CINE F 2013)",
            "cine_f_2013_ac_campo_especifico": "Campo Específico (CINE F 2013)",
            "cine_f_2013_ac_campo_detallado": "Campo Detallado (CINE F 2013)",
            "area_de_conocimiento": "Área de Conocimiento",
            "nucleo_basico_del_conocimiento": "Núcleo Básico del Conocimiento",
            "nivel_academico": "Nivel Académico",
            "nivel_de_formacion": "Nivel de Formación",
        }

class EditarNovedadesForm(forms.ModelForm):
    sugerencia_snies_text = forms.CharField(
        label='Buscar equivalente',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded px-3 py-1',
            'list': 'snies-titulos'
        })
    )

    class Meta:
        model = NovedadEquivalencia
        fields = [
            'descripcion',
            'id_vacante',
            'identificacion_candidato',
            'titulo',
        ]
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_vacante': forms.TextInput(attrs={'class': 'form-control'}),
            'identificacion_candidato': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }
