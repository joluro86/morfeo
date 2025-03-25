from django.db import models
from django.urls import reverse

class CampoAmplioPregrado(models.Model):
    descripcion = models.CharField(max_length=300, null=True, blank=True, default="", unique=True)

    class Meta:
        verbose_name = 'Campo Amplio Pregado'
        verbose_name_plural = 'Campos Amplios Pregrado'

    def __str__(self):
        return self.descripcion if self.descripcion else "Sin descripción"

    def save(self, *args, **kwargs):
        # Puedes agregar lógica adicional antes de guardar, si es necesario
        super().save(*args, **kwargs)  # Llama al método save original

    def get_absolute_url(self):
        return reverse('nombre_de_la_vista', kwargs={'pk': self.pk})  # Reemplaza con el nombre real de la vista


class CampoEspecificoPregrado(models.Model):
    descripcion = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name = 'Campo Especifico'
        verbose_name_plural = 'Campos Especificos'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('campo_especifico_detail', kwargs={'pk': self.pk})


class CampoDetalladoPregrado(models.Model):
    descripcion = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name = 'Campo Detallado'
        verbose_name_plural = 'Campos Detallados'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('campo_detallado_detail', kwargs={'pk': self.pk})


class NivelAcademico(models.Model):
    descripcion = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name = 'Nivel Académico'
        verbose_name_plural = 'Niveles Académicos'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('nivel_academico_detail', kwargs={'pk': self.pk})

class CampoAmplioPosgrado(models.Model):
    descripcion = models.CharField(max_length=300, null=True, blank=True, default="", unique=True)

    class Meta:
        verbose_name = 'Campo Amplio Posgrado'
        verbose_name_plural = 'Campos Amplios Posgrado'

    def __str__(self):
        return self.descripcion if self.descripcion else "Sin descripción"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('campo_amplio_posgrado_detail', kwargs={'pk': self.pk})


class CampoEspecificoPosgrado(models.Model):
    descripcion = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name = 'Campo Específico Posgrado'
        verbose_name_plural = 'Campos Específicos Posgrado'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('campo_especifico_posgrado_detail', kwargs={'pk': self.pk})

class CampoDetalladoPosgrado(models.Model):
    descripcion = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name = 'Campo Detallado Posgrado'
        verbose_name_plural = 'Campos Detallados Posgrado'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('campo_detallado_posgrado_detail', kwargs={'pk': self.pk})


class Vacante(models.Model):
    """Modelo para gestionar las vacantes según nivel académico"""
    numero = models.BigIntegerField(unique=True)  # Número único de la vacante
    nivel_academico = models.ForeignKey('NivelAcademico', on_delete=models.CASCADE, related_name='vacantes')

    def __str__(self):
        return f"Vacante {self.numero} - {self.nivel_academico}"


class Candidato(models.Model):
    id_vacante = models.IntegerField()
    identificacion = models.CharField(max_length=20, unique=False)
    nombre = models.CharField(max_length=255)
    es_interno = models.BooleanField()
    titulo = models.CharField(max_length=255)
    otro_titulo = models.CharField(max_length=255, blank=True, null=True)
    nivel_estudios = models.CharField(max_length=50)
    fecha_fin_estudios = models.CharField(max_length=20, blank=True, null=True)  # Ahora es CharField
    fecha_diploma = models.CharField(max_length=20, blank=True, null=True)  # Ahora es CharField
    cumple_requisitos = models.BooleanField(blank=True, null=True)
    justificacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.titulo} - {'Cumple' if self.cumple_requisitos else 'No cumple'}"
    

class ConfiguracionCandidato(models.Model):
    nombre = models.CharField(max_length=255, default="Configuración predeterminada")

    # Definir los índices de las columnas del archivo Excel
    col_id_vacante = models.IntegerField(default=0)
    col_identificacion = models.IntegerField(default=1)
    col_nombre = models.IntegerField(default=2)
    col_es_interno = models.IntegerField(default=3)
    col_titulo = models.IntegerField(default=4)
    col_otro_titulo = models.IntegerField(default=5)
    col_nivel_estudios = models.IntegerField(default=6)
    col_fecha_fin_estudios = models.IntegerField(default=7)
    col_fecha_diploma = models.IntegerField(default=8)

    def __str__(self):
        return f"Configuración de Candidato ({self.nombre})"


class ProgramaAcademicoSnies(models.Model):
    nombre_del_programa = models.CharField(max_length=500, blank=True, null=True)
    titulo_otorgado = models.CharField(max_length=500, blank=True, null=True)
    cine_f_2013_ac_campo_amplio = models.CharField(max_length=500, blank=True, null=True)
    cine_f_2013_ac_campo_especifico = models.CharField(max_length=500, blank=True, null=True)
    cine_f_2013_ac_campo_detallado = models.CharField(max_length=500, blank=True, null=True)
    area_de_conocimiento = models.CharField(max_length=255, blank=True, null=True)
    nucleo_basico_del_conocimiento = models.CharField(max_length=255, blank=True, null=True)
    nivel_academico = models.CharField(max_length=255, blank=True, null=True)
    nivel_de_formacion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_del_programa
    

class EquivalenciaTitulo(models.Model):
    titulo = models.CharField(max_length=500, blank=True, null=True)
    otro_titulo = models.CharField(max_length=500, blank=True, null=True)
    nivel_estudios = models.CharField(max_length=500, blank=True, null=True)
    equivalente_snies = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.titulo


class NovedadEquivalencia(models.Model):
    equivalencia = models.ForeignKey(EquivalenciaTitulo, on_delete=models.CASCADE, related_name='novedades')
    descripcion = models.TextField()
    sugerencia_snies = models.ForeignKey(
        'ProgramaAcademicoSnies',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='novedades_asignadas'
    )
    revisado = models.BooleanField(default=False)

    def __str__(self):
        return f"Novedad: {self.equivalencia.titulo}"


from .models import EquivalenciaTitulo, ProgramaAcademicoSnies, NovedadEquivalencia

def buscar_equivalencias_snies():
    palabras_excluir = ['bachiller', 'completar', 'posgrado', 'postgrado']

    equivalencias = EquivalenciaTitulo.objects.filter(equivalente_snies__isnull=True)

    for eq in equivalencias:
        titulo_base = (eq.titulo or '').lower()
        otro_titulo_base = (eq.otro_titulo or '').lower()

        # Ignorar títulos con palabras prohibidas
        if any(p in titulo_base for p in palabras_excluir) or any(p in otro_titulo_base for p in palabras_excluir):
            continue

        # Buscar coincidencias por título o por otro_titulo
        match = ProgramaAcademicoSnies.objects.filter(
            models.Q(titulo_otorgado__icontains=eq.titulo) |
            models.Q(nombre_del_programa__icontains=eq.titulo) |
            models.Q(titulo_otorgado__icontains=eq.otro_titulo) |
            models.Q(nombre_del_programa__icontains=eq.otro_titulo)
        ).first()

        if match:
            eq.equivalente_snies = match.titulo_otorgado
            eq.save()
        else:
            # Evitar duplicar novedades
            if not NovedadEquivalencia.objects.filter(equivalencia=eq).exists():
                NovedadEquivalencia.objects.create(
                    equivalencia=eq,
                    descripcion=f"No se encontró coincidencia para el título '{eq.titulo}'"
                )
