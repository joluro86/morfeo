from django.urls import path
from vacante.views_campo_amplio_pos import campo_amplio_posgrado_bulk_upload, campo_amplio_posgrado_create, campo_amplio_posgrado_delete, campo_amplio_posgrado_list
from vacante.views_campo_amplio_pre import campo_amplio_list, campo_amplio_create, campo_amplio_delete, campo_amplio_bulk_upload
from vacante.views_campo_detallado_pos import campo_detallado_posgrado_bulk_upload, campo_detallado_posgrado_create, campo_detallado_posgrado_delete, campo_detallado_posgrado_list
from vacante.views_campo_especifico_pos import campo_especifico_posgrado_bulk_upload, campo_especifico_posgrado_create, campo_especifico_posgrado_delete, campo_especifico_posgrado_list
from vacante.views_campo_especifico_pre import campo_especifico_list,  campo_especifico_create, campo_especifico_delete, campo_especifico_bulk_upload
from vacante.views_vacante import VacanteCreateView, VacanteDeleteView, VacanteListView, VacanteUpdateView, limpiar, index
from vacante.views_candidatos import cargar_candidatos, lista_candidatos, exportar_candidatos_excel, limpiar_candidatos
from vacante.views_subir_candidatos import editar_configuracion_candidato
from vacante.views_gestion_candidato import analizar_candidatos_bachiller, gestionar_candidatos
from vacante.views_snies import cargar_programas_academicos_snies

from .views_nivel_academico import (
    nivel_academico_list,
    nivel_academico_create,
    nivel_academico_delete,
    nivel_academico_bulk_upload
)

from .views_campo_detallado_pregrado import (
    campo_detallado_list,
    campo_detallado_create,
    campo_detallado_delete,
    campo_detallado_bulk_upload,
)

from vacante.views_snies import (
    cargar_programas_academicos_snies,
    lista_programas_academicos_snies,
    exportar_programas_snies_excel
)


urlpatterns = [
    path('', index, name='index'),
    path('campo_amplio/', campo_amplio_list, name='campo_amplio_list'),
    path('campo_amplio/nuevo/', campo_amplio_create, name='campo_amplio_create'),
    path('campo_amplio/eliminar/<int:pk>/', campo_amplio_delete, name='campo_amplio_delete'),
    path('campo_amplio/carga-masiva/', campo_amplio_bulk_upload, name='campo_amplio_bulk_upload'),
    
    path('campo_especifico/', campo_especifico_list, name='campo_especifico_list'),
    path('campo_especifico/nuevo/', campo_especifico_create, name='campo_especifico_create'),
    path('campo_especifico/eliminar/<int:pk>/', campo_especifico_delete, name='campo_especifico_delete'),
    path('campo_especifico/carga-masiva/', campo_especifico_bulk_upload, name='campo_especifico_bulk_upload'),

    path('nivel_academico/', nivel_academico_list, name='nivel_academico_list'),
    path('nivel_academico/nuevo/', nivel_academico_create, name='nivel_academico_create'),
    path('nivel_academico/eliminar/<int:pk>/', nivel_academico_delete, name='nivel_academico_delete'),
    path('nivel_academico/carga-masiva/', nivel_academico_bulk_upload, name='nivel_academico_bulk_upload'),
    
    path('campo_detallado_pregrado/', campo_detallado_list, name='campo_detallado_pregrado_list'),
    path('campo_detallado_pregrado/nuevo/', campo_detallado_create, name='campo_detallado_pregrado_create'),
    path('campo_detallado_pregrado/eliminar/<int:pk>/', campo_detallado_delete, name='campo_detallado_pregrado_delete'),
    path('campo_detallado_pregrado/carga-masiva/', campo_detallado_bulk_upload, name='campo_detallado_pregrado_bulk_upload'),

    # URLs para Campo Amplio Posgrado
    path('posgrado/campo-amplio/', campo_amplio_posgrado_list, name='campo_amplio_posgrado_list'),
    path('posgrado/campo-amplio/nuevo/', campo_amplio_posgrado_create, name='campo_amplio_posgrado_create'),
    path('posgrado/campo-amplio/eliminar/<int:pk>/', campo_amplio_posgrado_delete, name='campo_amplio_posgrado_delete'),
    path('posgrado/campo-amplio/carga-masiva/', campo_amplio_posgrado_bulk_upload, name='campo_amplio_posgrado_bulk_upload'),

    # URLs para Campo Específico Posgrado
    path('posgrado/campo-especifico/', campo_especifico_posgrado_list, name='campo_especifico_posgrado_list'),
    path('posgrado/campo-especifico/nuevo/', campo_especifico_posgrado_create, name='campo_especifico_posgrado_create'),
    path('posgrado/campo-especifico/eliminar/<int:pk>/', campo_especifico_posgrado_delete, name='campo_especifico_posgrado_delete'),
    path('posgrado/campo-especifico/carga-masiva/', campo_especifico_posgrado_bulk_upload, name='campo_especifico_posgrado_bulk_upload'),

    # URLs para Campo Detallado Posgrado
    path('posgrado/campo-detallado/', campo_detallado_posgrado_list, name='campo_detallado_posgrado_list'),
    path('posgrado/campo-detallado/nuevo/', campo_detallado_posgrado_create, name='campo_detallado_posgrado_create'),
    path('posgrado/campo-detallado/eliminar/<int:pk>/', campo_detallado_posgrado_delete, name='campo_detallado_posgrado_delete'),
    path('posgrado/campo-detallado/carga-masiva/', campo_detallado_posgrado_bulk_upload, name='campo_detallado_posgrado_bulk_upload'),

    # URLs para Vacante
    path('lista', VacanteListView.as_view(), name='lista_vacantes'),
    path('nueva/', VacanteCreateView.as_view(), name='crear_vacante'),
    path('editar/<int:pk>/', VacanteUpdateView.as_view(), name='editar_vacante'),
    path('eliminar/<int:pk>/', VacanteDeleteView.as_view(), name='eliminar_vacante'),
    path('limpiar/', limpiar, name="limpiar"),
    
    # URLs para Candidato
    path('candidatos/cargar/', cargar_candidatos, name='cargar_candidatos'),
    path('candidatos/lista/', lista_candidatos, name='lista_candidatos'),
    path('candidatos/exportar/', exportar_candidatos_excel, name='exportar_candidatos_excel'),
    path('candidatos/limpiar/', limpiar_candidatos, name='limpiar_candidatos'),
    path("candidatos/configuracion/", editar_configuracion_candidato, name="editar_configuracion_candidato"),
    
    # URLs para Gestion candidato
    path('bachiller/', analizar_candidatos_bachiller, name="gestionar_bachiller"),
    path('gestionar_candidatos/', gestionar_candidatos, name="gestionar_candidatos"),
    
    # URLs para Snies
    path("cargar-programas-snies/", cargar_programas_academicos_snies, name="cargar_programas_academicos_snies"),
    path('programas/cargar/', cargar_programas_academicos_snies, name='cargar_programas_academicos_snies'),
    path('programas/lista/', lista_programas_academicos_snies, name='lista_programas_academicos_snies'),
    path('programas/exportar/', exportar_programas_snies_excel, name='exportar_programas_snies_excel'),
]
