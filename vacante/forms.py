from django import forms
from .models import Vacante, CampoAmplioPregrado, CampoEspecificoPregrado, NivelAcademico, CampoDetalladoPregrado

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
