from django import forms
from .models import CampoAmplioPregrado, CampoEspecificoPregrado, NivelAcademico, CampoDetalladoPregrado

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