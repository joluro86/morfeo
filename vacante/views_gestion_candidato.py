from django.shortcuts import redirect
from vacante.models import Candidato


def gestionar_bachiller(request):
    try:
        # Filtrar solo los candidatos con nivel de estudios "Bachiller" y la vacante específica
        candidatos = Candidato.objects.filter(nivel_estudios="Bachiller")

        # Actualizar en bloque sin iterar uno a uno
        candidatos.update(cumple_requisitos=True)

    except Exception as e:
        print(f"Error en gestion_bachiller: {e}")

    return redirect("lista_candidatos")  # Redirigir a la lista después de la actualización

    
    