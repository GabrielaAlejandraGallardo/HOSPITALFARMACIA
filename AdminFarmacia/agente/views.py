from django.shortcuts import get_object_or_404, redirect, render

from deposito.models import Deposito

from .models import Agente, Especialidad


# Create your views here.
def inicio(request):
    return render(request, "pagina_base/inicio.html")


def lista_agentes(request):
    agentes = Agente.objects.all()
    return render(request, "lista_agentes.html", {"agentes": agentes})


def alta_agentes(request):
    if request.method == "POST":
        # Campos esperados por la plantilla `alta_agente.html`
        dni = request.POST["dni"]
        nombre_apellido = request.POST["nombre_apellido"]
        contacto = request.POST["contacto"]
        email = request.POST["email"]
        id_especialidad = request.POST["id_especialidad"]

        # Campos opcionales (por si tu formulario/envío los incluye)
        especialidad = Especialidad.objects.get(id_especialidad=id_especialidad)

        # Si el form incluye deposito, lo asociamos. Si no, evitamos romper.

        agente_existente = Agente.objects.filter(dni=dni).first()
        if agente_existente:
            especialidades = Especialidad.objects.all()
            return render(
                request,
                "alta_agente.html",
                {
                    "especialidades": especialidades,
                    "error": "Ya existe un agente con ese DNI.",
                },
                status=400,
            )

        nuevo_agente = Agente(
            dni=dni,
            nombre_apellido=nombre_apellido,
            contacto=contacto,
            email=email,
            id_especialidad=especialidad,
        )
        nuevo_agente.save()
        return redirect("lista_agentes")

    especialidades = Especialidad.objects.all()
    return render(request, "alta_agente.html", {"especialidades": especialidades})


def eliminacion_agentes(request, id_agente):
    agente = Agente.objects.get(id_agente=id_agente)
    agente.delete()
    agentes = Agente.objects.all()
    return render(request, "lista_agentes.html", {"agentes": agentes})


Especialidad


def modificaciones_agentes(request, id_agente):
    agente = get_object_or_404(Agente, id_agente=id_agente)
    especialidades = Especialidad.objects.all()

    if request.method == "POST":
        agente.dni = request.POST["dni"]
        agente.nombre_apellido = request.POST["nombre_apellido"]
        agente.contacto = request.POST["contacto"]
        agente.id_especialidad_id = request.POST["id_especialidad"]
        agente.email = request.POST["email"]
        agente.save()
        # ✅ redirige a la lista después de guardar
        return redirect("lista_agentes")

    return render(
        request,
        "modificacion_agente.html",
        {"agente": agente, "especialidades": especialidades},
    )
