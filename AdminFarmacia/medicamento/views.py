from django.shortcuts import render, redirect
from .models import *
from deposito.models import Deposito, Hueco, Supervisor


# Create your views here.
def inicio(request):
    return render(request, "pagina_base/inicio.html")


# --- Medicamentos ---

def lista_medicamento(request):
    medicamentos = Medicamento.objects.all()
    return render(request, "lista_medicamento.html", {"depositos": medicamentos})


def alta_medicamento(request):
    if request.method == "POST":
        description = request.POST.get("description")
        fecha_vencimiento = request.POST.get("fecha_vencimiento")
        lote = request.POST.get("lote")
        fecha_ingreso = request.POST.get("fecha_ingreso")
        deposito_id = request.POST.get("deposito")
        fecha_dispensa = request.POST.get("fecha_dispensa")
        qr = request.POST.get("qr")
        cod_barra = request.POST.get("cod_barra")
        estado_id = request.POST.get("id_estado")
        refrigeracion = request.POST.get("refrigeracion")
        nivel_id = request.POST.get("id_nivel_de_riesgo")
        cantidad_stock = request.POST.get("cantidad_stock")

        if all([description, fecha_vencimiento, lote, fecha_ingreso, deposito_id, fecha_dispensa, cod_barra, estado_id, refrigeracion, nivel_id, cantidad_stock]):
            medicamento = Medicamento(
                description=description,
                fecha_vencimiento=fecha_vencimiento,
                lote=lote,
                fecha_ingreso=fecha_ingreso,
                id_deposito_id=deposito_id,
                fecha_dispensa=fecha_dispensa,
                qr=qr or None,
                cod_barra=cod_barra,
                id_estado_id=estado_id,
                refrigeracion=refrigeracion,
                id_nivel_de_riesgo_id=nivel_id,
                cant_stock=cantidad_stock,
            )
            medicamento.save()
        return redirect("lista_medicamento")

    depositos = Deposito.objects.all()
    estados = Estado_medicamento.objects.all()
    niveles = Nivel_Riesgo.objects.all()
    return render(request, "alta_medicamento.html", {"depositos": depositos, "estados": estados, "niveles": niveles})


def eliminacion_medicamento(request, id_medicamento):
    medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
    if request.method == "POST":
        medicamento.delete()
        return redirect("lista_medicamento")
    return render(request, "elimina_medicamento.html", {"deposito": medicamento})


def modificaciones_medicamento(request, id_medicamento):
    medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
    if request.method == "POST":
        medicamento.save()
        return redirect("lista_medicamento")
    return render(request, "modificacion_deposito.html", {"deposito": medicamento})


# --- Hueco / Supervisor ---
# Estas vistas existen en urls.py, pero en tu views.py no estaban implementadas.
# Se agregan implementaciones mínimas para que el proyecto inicie.

def lista_hueco(request):
    huecos = Hueco.objects.all()
    return render(request, "lista_hueco.html", {"huecos": huecos})


def alta_hueco(request):
    if request.method == "POST":
        Hueco.objects.create(
            descripcion=request.POST.get("descripcion", "")
        )
        return redirect("lista_hueco")
    return render(request, "alta_hueco.html")


def eliminacion_hueco(request, id_hueco):
    hueco = Hueco.objects.get(id_hueco=id_hueco)
    if request.method == "POST":
        hueco.delete()
        return redirect("lista_hueco")
    return render(request, "eliminacion_hueco.html", {"hueco": hueco})


def modificaciones_hueco(request, id_hueco):
    hueco = Hueco.objects.get(id_hueco=id_hueco)
    if request.method == "POST":
        hueco.descripcion = request.POST.get("descripcion", hueco.descripcion)
        hueco.save()
        return redirect("lista_hueco")
    return render(request, "modificacion_hueco.html", {"hueco": hueco})


def lista_supervisor(request):
    supervisores = Supervisor.objects.all()
    return render(request, "lista_supervisor.html", {"supervisores": supervisores})


def alta_supervisor(request):
    if request.method == "POST":
        Supervisor.objects.create(
            nombre_apellido=request.POST.get("nombre_apellido", ""),
            contacto=request.POST.get("contacto", ""),
        )
        return redirect("lista_supervisor")
    return render(request, "alta_supervisor.html")


def eliminacion_supervisor(request, id_supervisor):
    supervisor = Supervisor.objects.get(id_supervisor=id_supervisor)
    if request.method == "POST":
        supervisor.delete()
        return redirect("lista_supervisor")
    return render(request, "eliminacion_supervisor.html", {"supervisor": supervisor})


def modificacion_supervisor(request, id_supervisor):
    supervisor = Supervisor.objects.get(id_supervisor=id_supervisor)
    if request.method == "POST":
        supervisor.nombre_apellido = request.POST.get("nombre_apellido", supervisor.nombre_apellido)
        supervisor.contacto = request.POST.get("contacto", supervisor.contacto)
        supervisor.save()
        return redirect("lista_supervisor")
    return render(request, "modificacion_supervisor.html", {"supervisor": supervisor})

