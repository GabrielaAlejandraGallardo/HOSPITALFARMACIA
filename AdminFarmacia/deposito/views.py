from collections import defaultdict
from tempfile import template
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from matplotlib.style import context
from .models import *


# Create your views here.
def inicio(request):
    return render(request, "pagina_base/inicio.html")


# funciones para deposito
def lista_deposito(request):
    Deposito


def lista_deposito(request):
    depositos = Deposito.objects.all()
    return render(request, "lista_deposito.html", {"depositos": depositos})


def alta_deposito(request):
    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        id_supervisor = request.POST.get("id_supervisor")  # Obtener el ID del supervisor seleccionado
        supervisor = Supervisor.objects.get(id_supervisor=id_supervisor)  # Obtener el objeto Supervisor
        if descripcion:  # Validación básica
            deposito = Deposito(descripcion=descripcion)
            deposito.id_supervisor = supervisor  # Asignar el supervisor al depósito
            deposito.save()
        return redirect("lista_deposito")  # Redirige a la vista que lista depósitos

    # Si es GET, mostramos la lista de depósitos y supervisores
    depositos = Deposito.objects.all()
    supervisores = Supervisor.objects.all()
    return render(
        request,
        "alta_deposito.html",
        {"depositos": depositos, "supervisores": supervisores},
    )


def eliminacion_deposito(request, id_deposito):
    deposito = Deposito.objects.get(id_deposito=id_deposito)

    if request.method == "POST":
        deposito.delete()
        return redirect("lista_deposito")

    return render(request, "elimina_deposito.html", {"deposito": deposito})


def modificaciones_deposito(request, id_deposito):
    deposito = Deposito.objects.get(id_deposito=id_deposito)
    

    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        id_supervisor = request.POST.get("id_supervisor")  # Obtener el ID del supervisor seleccionado

        if descripcion:
            deposito.descripcion = descripcion

        # Solo actualiza el supervisor si viene informado en el formulario.
        if id_supervisor:
            supervisor = Supervisor.objects.get(id_supervisor=id_supervisor)
            deposito.id_supervisor = supervisor

        deposito.save()
        return redirect("lista_deposito")
        return redirect("lista_deposito")

    return render(request, "modificacion_deposito.html", {"deposito": deposito})


# Funciones para hueco
def lista_hueco(request):
    huecos = Hueco.objects.all()
    return render(request, "lista_hueco.html", {"huecos": huecos})


def alta_hueco(request):
    pass


def eliminacion_hueco(request, id_hueco):
    pass


def modificaciones_hueco(request, id_hueco):
    pass


# funciones para Supervisor
def lista_supervisor(request):
    supervisores = Supervisor.objects.all()
    return render(request, "lista_supervisor.html", {"supervisores": supervisores})


def alta_supervisor(request):
    if request.method == "POST":
        nombre_apellido = request.POST.get("nombre_apellido")
        contacto = request.POST.get("contacto")

        if nombre_apellido and contacto:
            Supervisor.objects.create(
                nombre_apellido=nombre_apellido,
                contacto=contacto,
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
        nombre_apellido = request.POST.get("nombre_apellido")
        contacto = request.POST.get("contacto")
        if nombre_apellido and contacto:
            supervisor.nombre_apellido = nombre_apellido
            supervisor.contacto = contacto
            supervisor.save()
            return redirect("lista_supervisor")

    return render(request, "modificacion_supervisor.html", {"supervisor": supervisor})  

