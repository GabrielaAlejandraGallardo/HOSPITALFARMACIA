from django.shortcuts import render, redirect
from .models import Remito, RemitoMedicamento, RemitoDescartable
from deposito.models import Deposito
from medicamento.models import Medicamento
from descartable.models import Descartable


def inicio(request):
    return render(request, "pagina_base/inicio.html")


def lista_remito(request):
    remitos = Remito.objects.all().order_by("-fecha_emision")
    return render(request, "listado_remito.html", {"remitos": remitos})


def alta_remito(request):
    if request.method == "POST":
        id_deposito_origen = request.POST.get("id_deposito_origen")
        id_deposito_destino = request.POST.get("id_deposito_destino")
        observaciones = request.POST.get("observaciones", "")

        remito = Remito.objects.create(
            id_deposito_origen_id=id_deposito_origen,
            id_deposito_destino_id=id_deposito_destino,
            observaciones=observaciones or None,
        )

        # Procesar medicamentos
        medicamento_ids = request.POST.getlist("medicamento_ids[]")
        medicamento_cantidades = request.POST.getlist("medicamento_cantidades[]")

        for med_id, cant in zip(medicamento_ids, medicamento_cantidades):
            if med_id and cant:
                try:
                    med = Medicamento.objects.get(id_medicamento=med_id)
                    cantidad = int(cant)
                    if cantidad > 0 and cantidad <= med.cant_stock:
                        RemitoMedicamento.objects.create(
                            id_remito=remito,
                            id_medicamento=med,
                            cantidad=cantidad,
                        )
                        # Descontar stock
                        med.cant_stock -= cantidad
                        med.save()
                except (Medicamento.DoesNotExist, ValueError):
                    continue

        # Procesar descartables
        descartable_ids = request.POST.getlist("descartable_ids[]")
        descartable_cantidades = request.POST.getlist("descartable_cantidades[]")

        for desc_id, cant in zip(descartable_ids, descartable_cantidades):
            if desc_id and cant:
                try:
                    desc = Descartable.objects.get(id_descartable=desc_id)
                    cantidad = int(cant)
                    if cantidad > 0 and cantidad <= desc.cant_stock:
                        RemitoDescartable.objects.create(
                            id_remito=remito,
                            id_descartable=desc,
                            cantidad=cantidad,
                        )
                        # Descontar stock
                        desc.cant_stock -= cantidad
                        desc.save()
                except (Descartable.DoesNotExist, ValueError):
                    continue

        return redirect("lista_remito")

    depositos = Deposito.objects.all()
    medicamentos = Medicamento.objects.filter(cant_stock__gt=0)
    descartables = Descartable.objects.filter(cant_stock__gt=0)

    return render(
        request,
        "alta_remito.html",
        {
            "depositos": depositos,
            "medicamentos": medicamentos,
            "descartables": descartables,
        },
    )


def modificacion_remito(request, id_remito):
    remito = Remito.objects.get(id_remito=id_remito)
    items_medicamentos = RemitoMedicamento.objects.filter(id_remito=remito)
    items_descartables = RemitoDescartable.objects.filter(id_remito=remito)

    if request.method == "POST":
        remito.id_deposito_origen_id = request.POST.get("id_deposito_origen")
        remito.id_deposito_destino_id = request.POST.get("id_deposito_destino")
        remito.observaciones = request.POST.get("observaciones", "") or None
        remito.save()

        return redirect("lista_remito")

    depositos = Deposito.objects.all()
    return render(
        request,
        "modificacion_remito.html",
        {
            "remito": remito,
            "depositos": depositos,
            "items_medicamentos": items_medicamentos,
            "items_descartables": items_descartables,
        },
    )


def eliminacion_remito(request, id_remito):
    remito = Remito.objects.get(id_remito=id_remito)

    if request.method == "POST":
        # Restaurar stock de medicamentos
        for item in RemitoMedicamento.objects.filter(id_remito=remito):
            med = item.id_medicamento
            med.cant_stock += item.cantidad
            med.save()
        # Restaurar stock de descartables
        for item in RemitoDescartable.objects.filter(id_remito=remito):
            desc = item.id_descartable
            desc.cant_stock += item.cantidad
            desc.save()
        remito.delete()
        return redirect("lista_remito")

    return render(request, "eliminacion_remito.html", {"remito": remito})

