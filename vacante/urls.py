from django.urls import path
from vacante.views_campo_amplio_pos import campo_amplio_posgrado_bulk_upload, campo_amplio_posgrado_create, campo_amplio_posgrado_delete, campo_amplio_posgrado_list
from vacante.views_campo_amplio_pre import campo_amplio_list, campo_amplio_create, campo_amplio_delete, campo_amplio_bulk_upload
from vacante.views_campo_detallado_pos import campo_detallado_posgrado_bulk_upload, campo_detallado_posgrado_create, campo_detallado_posgrado_delete, campo_detallado_posgrado_list
from vacante.views_campo_especifico_pos import campo_especifico_posgrado_bulk_upload, campo_especifico_posgrado_create, campo_especifico_posgrado_delete, campo_especifico_posgrado_list
from vacante.views_campo_especifico_pre import campo_especifico_list,  campo_especifico_create, campo_especifico_delete, campo_especifico_bulk_upload
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


urlpatterns = [
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

]
