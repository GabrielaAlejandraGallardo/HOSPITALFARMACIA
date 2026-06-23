from django.shortcuts import render, redirect
from .models import *
from deposito.models import Deposito, Hueco, Supervisor
from medicamento.models import (
<<<<<<< HEAD
    Laboratorio,
    Nivel_Riesgo,
    Refrigeracion,
    Dispensa,
)
from datetime import datetime
from medicamento.models import Estado_medicamento, Nivel_Riesgo, Refrigeracion, Laboratorio
from deposito.models import Deposito
from .models import Descartable

=======
    Medicamento,
)
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89

from django.conf import settings

from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from django.db.models import Sum, Count


<<<<<<< HEAD

def reporte_diario(request):
    hoy = timezone.now().date()

    # Descartables ingresados hoy
=======
def reporte_diario(request):
    hoy = timezone.now().date()

    # Medicamentos ingresados hoy
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
    ingresados_hoy = Descartable.objects.filter(fecha_ingreso=hoy)

    # Medicamentos dispensados hoy
    dispensas_hoy = Dispensa.objects.filter(fecha__date=hoy)

    # Totales
    total_ingresados = ingresados_hoy.count()
    total_dispensados = dispensas_hoy.aggregate(total=Sum("cantidad"))["total"] or 0

    # Agrupar dispensas por medicamento (usando id, no description)
    dispensas_por_medicamento = (
<<<<<<< HEAD
        dispensas_hoy
        .values("id_descartable")  # <--- cambiado
=======
        dispensas_hoy.values("id_descartable")  # <--- cambiado
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
        .annotate(total=Sum("cantidad"))
        .order_by("-total")
    )

    # Convertir a lista de dicts con el nombre legible
    dispensas_lista = []
    for item in dispensas_por_medicamento:
        med = Descartable.objects.get(id_descartable=item["id_descartable"])
<<<<<<< HEAD
        dispensas_lista.append({
            "descartable": med.description,
            "total": item["total"],
        })

    return render(request, "reporte_diario.html", {
        "hoy": hoy,
        "ingresados_hoy": ingresados_hoy,
        "dispensas_hoy": dispensas_hoy,
        "total_ingresados": total_ingresados,
        "total_dispensados": total_dispensados,
        "dispensas_por_medicamento": dispensas_lista,  # <--- ahora pasa la lista procesada
    })

def medicamentos_mas_dispensados(request):
=======
        dispensas_lista.append(
            {
                "descartable": med.description,
                "total": item["total"],
            }
        )

    return render(
        request,
        "reporte_diario.html",
        {
            "hoy": hoy,
            "ingresados_hoy": ingresados_hoy,
            "dispensas_hoy": dispensas_hoy,
            "total_ingresados": total_ingresados,
            "total_dispensados": total_dispensados,
            "dispensas_por_medicamento": dispensas_lista,  # <--- ahora pasa la lista procesada
        },
    )


def descartable_mas_dispensados(request):
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
    # Calcular la fecha de hace una semana
    una_semana_atras = timezone.now() - timedelta(days=7)

    # Agrupar dispensas por medicamento y sumar cantidades en la última semana
    dispensas = (
<<<<<<< HEAD
        Dispensa.objects
        .filter(fecha__gte=una_semana_atras)
=======
        Dispensa.objects.filter(fecha__gte=una_semana_atras)
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
        .values("id_descartable__id_descartable", "id_descartable__description")
        .annotate(total_dispensado=Sum("cantidad"))
        .order_by("-total_dispensado")
    )

<<<<<<< HEAD
    return render(request, "medicamentos_mas_dispensados.html", {"dispensas": dispensas})
=======
    return render(
        request, "medicamentos_mas_dispensados.html", {"dispensas": dispensas}
    )

>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89

# Create your views here.
def inicio(request):
    return render(request, "pagina_base/inicio.html")


<<<<<<< HEAD

from django.shortcuts import render
from .models import Descartable

def lista_descartable(request):
    descartables = Descartable.objects.all()
    return render(request, "lista_descartable.html", {
    "descartables": descartables
})


def buscar_descartable(request):
    query = request.GET.get("descripcion", "")
    descartables = Descartable.objects.all()

    if query:
        descartables = Descartable.objects.filter(description__icontains=query)

    return render(request, "lista_descartable.html", {
        "descartables": descartables
    })


=======
# --- Medicamentos ---


def lista_descartable(request):
    descartables = Descartable.objects.all()
    return render(request, "lista_descartable.html", {"descartables": descartables})
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89


def alta_descartable(request):
    if request.method == "POST":
        description = request.POST.get("description")
<<<<<<< HEAD
        laboratorio_id = request.POST.get("laboratorio")  # CORREGIDO
=======
        laboratorio_id = request.POST.get("laboratorio")
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
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
        cantidad_stock = request.POST.get("cant_stock")

<<<<<<< HEAD
        descartable = Descartable(
            description=description,
            id_laboratorio_id=laboratorio_id,  # CORREGIDO
            fecha_vencimiento=fecha_vencimiento,
            lote=lote,
            fecha_ingreso=fecha_ingreso,
            id_deposito_id=deposito_id,
            fecha_dispensa=fecha_dispensa,
            qr=qr or None,
            cod_barra=cod_barra,
            id_estado_id=estado_id,
            refrigeracion_id=refrigeracion,
            id_nivel_de_riesgo_id=nivel_id,
            cant_stock=cantidad_stock,
=======
        errores = []

        def _to_int_or_none(value):
            if value is None:
                return None
            value = str(value).strip()
            if value == "":
                return None
            try:
                return int(value)
            except (TypeError, ValueError):
                return None

        laboratorio_id_int = _to_int_or_none(laboratorio_id)
        deposito_id_int = _to_int_or_none(deposito_id)
        estado_id_int = _to_int_or_none(estado_id)
        refrigeracion_id_int = _to_int_or_none(refrigeracion)
        nivel_id_int = _to_int_or_none(nivel_id)

        # Validaciones de existencia
        if (
            deposito_id_int is None
            or not Deposito.objects.filter(id_deposito=deposito_id_int).exists()
        ):
            errores.append(f"Depósito inválido o no existe (id={deposito_id_int}).")

        if (
            estado_id_int is None
            or not Estado_descartable.objects.filter(id_estado=estado_id_int).exists()
        ):
            errores.append(f"Estado inválido o no existe (id={estado_id_int}).")

        if (
            nivel_id_int is None
            or not Nivel_Riesgo.objects.filter(id_nivel_de_riesgo=nivel_id_int).exists()
        ):
            errores.append(f"Nivel de riesgo inválido o no existe (id={nivel_id_int}).")

        if (
            laboratorio_id_int is not None
            and not Laboratorio.objects.filter(
                id_laboratorio=laboratorio_id_int
            ).exists()
        ):
            errores.append(f"Laboratorio no existe (id={laboratorio_id_int}).")

        if errores:
            return render(
                request,
                "alta_descartable.html",
                {
                    "depositos": Deposito.objects.all(),
                    "laboratorios": Laboratorio.objects.all(),
                    "estados": Estado_descartable.objects.all(),  # CORREGIDO
                    "niveles": Nivel_Riesgo.objects.all(),
                    "refrigeracion": Refrigeracion.objects.all(),
                    "error": "\n".join(errores),
                    "prefill": request.POST,
                },
                status=400,
            )

        # Conversión de numéricos
        cod_barra_int = (
            int(cod_barra) if cod_barra and str(cod_barra).strip() != "" else None
        )
        cantidad_stock_int = (
            int(cantidad_stock)
            if cantidad_stock and str(cantidad_stock).strip() != ""
            else None
        )

        descartable = Descartable(
            description=description,
            id_laboratorio_id=laboratorio_id_int,
            fecha_vencimiento=fecha_vencimiento,
            lote=lote,
            fecha_ingreso=fecha_ingreso,
            id_deposito_id=deposito_id_int,
            fecha_dispensa=fecha_dispensa,
            qr=qr or None,
            cod_barra=cod_barra_int,
            id_estado_id=estado_id_int,  # CORREGIDO → Estado_descartable
            refrigeracion_id=refrigeracion_id_int,
            id_nivel_de_riesgo_id=nivel_id_int,
            cant_stock=cantidad_stock_int,
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
        )
        descartable.save()
        return redirect("lista_descartable")

<<<<<<< HEAD
    depositos = Deposito.objects.all()
    estados = Estado_medicamento.objects.all()
    niveles = Nivel_Riesgo.objects.all()
    laboratorios = Laboratorio.objects.all()  # CORREGIDO
    refrigeracion = Refrigeracion.objects.all()

=======
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
    return render(
        request,
        "alta_descartable.html",
        {
<<<<<<< HEAD
            "depositos": depositos,
            "laboratorios": laboratorios,  # CORREGIDO
            "estados": estados,
            "niveles": niveles,
            "refrigeracion": refrigeracion,
=======
            "depositos": Deposito.objects.all(),
            "laboratorios": Laboratorio.objects.all(),
            "estados": Estado_descartable.objects.all(),  # CORREGIDO
            "niveles": Nivel_Riesgo.objects.all(),
            "refrigeracion": Refrigeracion.objects.all(),
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
        },
    )


<<<<<<< HEAD

=======
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
def eliminacion_descartable(request, id_descartable):
    descartable = Descartable.objects.get(id_descartable=id_descartable)
    if request.method == "POST":
        descartable.delete()
        return redirect("lista_descartable")
    return render(request, "elimina_descartable.html", {"descartable": descartable})


def modificaciones_descartable(request, id_descartable):
    descartable = Descartable.objects.get(id_descartable=id_descartable)
    if request.method == "POST":
<<<<<<< HEAD
        descartable = request.POST.get("description")
=======
        descartable.description = request.POST.get("description")
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
        descartable.laboratorio_id = request.POST.get("laboratorio")
        descartable.fecha_vencimiento = request.POST.get("fecha_vencimiento")
        descartable.lote = request.POST.get("lote")
        descartable.fecha_ingreso = request.POST.get("fecha_ingreso")
        descartable.id_deposito_id = request.POST.get("deposito")
        descartable.fecha_dispensa = request.POST.get("fecha_dispensa")
        descartable.qr = request.POST.get("qr") or None
        descartable.cod_barra = request.POST.get("cod_barra")
        descartable.id_estado_id = request.POST.get("id_estado")
        descartable.refrigeracion = request.POST.get("refrigeracion")
        descartable.id_nivel_de_riesgo_id = request.POST.get("id_nivel_de_riesgo")
        descartable.cant_stock = request.POST.get("cantidad_stock")
        descartable.save()
        return redirect("lista_descartable")

    depositos = Deposito.objects.all()
<<<<<<< HEAD
    estados = Estado_medicamento.objects.all()
=======
    estados = Estado_descartable.objects.all()
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
    niveles = Nivel_Riesgo.objects.all()
    refrigeracion = Refrigeracion.objects.all()
    return render(
        request,
<<<<<<< HEAD
        "modificacion_medicamento.html",
=======
        "modificacion_descartable.html",
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
        {
            "descartable": descartable,
            "laboratorios": Laboratorio.objects.all(),
            "depositos": depositos,
            "estados": estados,
            "refrigeracion": refrigeracion,
            "niveles": niveles,
        },
    )


# --- Hueco / Supervisor ---
# Estas vistas existen en urls.py, pero en tu views.py no estaban implementadas.
# Se agregan implementaciones mínimas para que el proyecto inicie.


def lista_hueco(request):
    huecos = Hueco.objects.all()
    return render(request, "lista_hueco.html", {"huecos": huecos})


def alta_hueco(request):
    if request.method == "POST":
        Hueco.objects.create(descripcion=request.POST.get("descripcion", ""))
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
        supervisor.nombre_apellido = request.POST.get(
            "nombre_apellido", supervisor.nombre_apellido
        )
        supervisor.contacto = request.POST.get("contacto", supervisor.contacto)
        supervisor.save()
        return redirect("lista_supervisor")
    return render(request, "modificacion_supervisor.html", {"supervisor": supervisor})


def lista_laboratorio(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, "lista_laboratorio.html", {"laboratorios": laboratorios})


def alta_laboratorio(request):
    if request.method == "POST":
        Laboratorio.objects.create(descripcion=request.POST.get("descripcion", ""))
        return redirect("lista_laboratorio")
    return render(request, "alta_laboratorio.html")


def eliminacion_laboratorio(request, id_laboratorio):
    laboratorio = Laboratorio.objects.get(id_laboratorio=id_laboratorio)
    if request.method == "POST":
        laboratorio.delete()
        return redirect("lista_laboratorio")
    return render(request, "eliminacion_laboratorio.html", {"laboratorio": laboratorio})


def modificaciones_laboratorio(request, id_laboratorio):
    laboratorio = Laboratorio.objects.get(id_laboratorio=id_laboratorio)
    if request.method == "POST":
        laboratorio.descripcion = request.POST.get(
            "descripcion", laboratorio.descripcion
        )
        laboratorio.save()
        return redirect("lista_laboratorio")
    return render(
        request, "modificacion_laboratorio.html", {"laboratorio": laboratorio}
    )

<<<<<<< HEAD
def realizar_dispensa(request, id_descartable):
    descartable = Descartable.objects.get(id_descartable=id_descartable)
=======

def realizar_dispensa(request, id_medicamento):
    medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89

    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 0))

        if cantidad <= 0:
<<<<<<< HEAD
            return render(request, "dispensa.html", {
                "descartable": descartable,
                "error": "La cantidad debe ser mayor a cero.",
            })

        if cantidad > descartable.cant_stock:
            return render(request, "dispensa.html", {
                "descartable": descartable,
                "error": f"Stock insuficiente. Stock actual: {descartable.cant_stock}",
            })

        # Crear el registro de dispensa
        Dispensa.objects.create(
            id_descartable=descartable,
=======
            return render(
                request,
                "dispensa.html",
                {
                    "medicamento": medicamento,
                    "error": "La cantidad debe ser mayor a cero.",
                },
            )

        if cantidad > medicamento.cant_stock:
            return render(
                request,
                "dispensa.html",
                {
                    "medicamento": medicamento,
                    "error": f"Stock insuficiente. Stock actual: {medicamento.cant_stock}",
                },
            )

        # Crear el registro de dispensa
        Dispensa.objects.create(
            id_medicamento=medicamento,
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
            cantidad=cantidad,
        )

        # Descontar del stock
<<<<<<< HEAD
        descartable.cant_stock -= cantidad
        descartable.save()

        return redirect("lista_descartable")

    return render(request, "dispensa.html", {"descartable": descartable})
=======
        medicamento.cant_stock -= cantidad
        medicamento.save()

        return redirect("lista_medicamento")

    return render(request, "dispensa.html", {"medicamento": medicamento})
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
