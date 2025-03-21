from django.shortcuts import redirect
from vacante.models import Candidato, Vacante

def gestionar_candidatos(request):
    """
    Analiza todas las vacantes y determina qué candidatos cumplen los requisitos.
    """
    vacantes = Vacante.objects.all()  # Obtener todas las vacantes

    for vacante in vacantes:
        nivel_requerido = vacante.nivel_academico.descripcion.strip()  # Obtener el nivel académico requerido
        
        # Si la vacante requiere "Bachiller", analizamos los candidatos correspondientes
        if nivel_requerido == "Bachiller":
            print(f"🔍 Analizando candidatos para vacante {vacante.numero} (Requiere: {nivel_requerido})")
            analizar_candidatos_bachiller(vacante.numero)
        
        if nivel_requerido == "Universitario":
            print(f"🔍 Analizando candidatos para vacante {vacante.numero} (Requiere: {nivel_requerido})")
            analizar_candidatos_universitario(vacante.numero)
    
    return redirect('lista_candidatos')

def analizar_candidatos_bachiller(numero_vacante):
    """
    Marca como 'cumple_requisitos=True' a los candidatos con nivel de estudios 'Bachiller'
    en la vacante dada.
    """
    print(numero_vacante)
    candidatos = Candidato.objects.filter(id_vacante=numero_vacante)  # Filtrar candidatos por vacante

    for candidato in candidatos:
        if candidato.nivel_estudios.strip() == "Bachiller":
            print(f"✅ {candidato.nombre} cumple con los requisitos para la vacante {numero_vacante}")
            candidato.cumple_requisitos = True
            candidato.save()  # Guardar el cambio en la base de datos
        else:
            candidato.justificacion= "No cumple titulo de Bachiller"
            candidato.save()


def analizar_candidatos_universitario(numero_vacante):
    """
    Marca como 'cumple_requisitos=True' a los candidatos con nivel de estudios 'Bachiller'
    en la vacante dada.
    """
    print(numero_vacante)
    candidatos = Candidato.objects.filter(id_vacante=numero_vacante)  # Filtrar candidatos por vacante

    for candidato in candidatos:
        if candidato.nivel_estudios.strip() == "Universitario":
            print(f"✅ {candidato.nombre} cumple con los requisitos para la vacante {numero_vacante}")
            candidato.cumple_requisitos = True
            candidato.save()  # Guardar el cambio en la base de datos
        else:
            candidato.justificacion= "No cumple titulo de Universitario"
            candidato.save()

     
    