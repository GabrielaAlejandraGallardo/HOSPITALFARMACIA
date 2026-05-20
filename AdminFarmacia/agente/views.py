from django.shortcuts import redirect, render
from .models import Agente, Especialidad

# Create your views here.
def inicio(request):
    return render(request, 'pagina_base/inicio.html')


def lista_agentes(request):
    agentes = Agente.objects.all()
    return render(request, 'lista_agentes.html', {'agentes': agentes})


def alta_agentes(request):
    # Consultar especialidades para poder renderizar el <select>
    especialidades = Especialidad.objects.all()

    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre_apellido = request.POST.get('nombre_apellido')
        contacto = request.POST.get('contacto')
        id_especialidad = request.POST.get('id_especialidad')
        email = request.POST.get('email')

        if dni and nombre_apellido and contacto and id_especialidad and email:
            agente = Agente(
                dni=dni,
                nombre_apellido=nombre_apellido,
                contacto=contacto,
                id_especialidad_id=id_especialidad,
                email=email,
            )
            agente.save()
            return render(request, 'alta_agentes.html', {'agente': agente, 'especialidades': especialidades})

    # Importante: siempre devolver HttpResponse (evita que retorne None en GET o POST inválido)
    return render(request, 'alta_agentes.html', {'agente': None, 'especialidades': especialidades})


def eliminacion_agentes(request, id_agente):
    agente = Agente.objects.get(id_agente=id_agente)

    if request.method == 'POST':
        agente.delete()
        return redirect('lista_agentes')

    return render(request, 'eliminacion_agentes.html', {'agente': agente})


def modificaciones_agentes(request, id_agente):
    agente = Agente.objects.get(id_agente=id_agente)
    especialidades = Especialidad.objects.all()

    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre_apellido = request.POST.get('nombre_apellido')
        contacto = request.POST.get('contacto')
        id_especialidad = request.POST.get('id_especialidad')
        email = request.POST.get('email')

        if dni and nombre_apellido and contacto and id_especialidad and email:  # Validación básica
            agente.dni = dni
            agente.nombre_apellido = nombre_apellido
            agente.contacto = contacto
            agente.id_especialidad_id = id_especialidad
            agente.email = email
            agente.save()
            return redirect('lista_agentes')

    return render(
        request,
        'modificaciones_agentes.html',
        {
            'agente': agente,
            'especialidades': especialidades,
        },
    )


def lista_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'lista_especialidades.html', {'especialidades': especialidades})


def alta_especialidades(request):
    if request.method == 'POST':
        nombre_especialidad = request.POST.get('nombre_especialidad')

        if nombre_especialidad:  # Validación básica
            especialidad = Especialidad(nombre_especialidad=nombre_especialidad)
            especialidad.save()
            return render(request, 'alta_especialidades.html', {'especialidad': especialidad})

    return render(request, 'alta_especialidades.html', {'especialidad': None})

