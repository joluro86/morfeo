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

