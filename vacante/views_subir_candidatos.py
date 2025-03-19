from django.shortcuts import render, redirect
from .models import ConfiguracionCandidato
from .forms import ConfiguracionCandidatoForm

def editar_configuracion_candidato(request):
    # Obtener la configuración existente o crear una nueva por defecto
    configuracion, created = ConfiguracionCandidato.objects.get_or_create(id=1)

    if request.method == "POST":
        form = ConfiguracionCandidatoForm(request.POST, instance=configuracion)
        if form.is_valid():
            form.save()
            return redirect("editar_configuracion_candidato")  # Redirigir a la misma página después de guardar

    else:
        form = ConfiguracionCandidatoForm(instance=configuracion)

    return render(request, "configuracion_subir_candidato.html", {"form": form})
