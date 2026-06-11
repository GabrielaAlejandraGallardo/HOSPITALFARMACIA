from django.contrib import admin

from .models import Agente, Especialidad


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ("id_especialidad", "nombre_especialidad")


@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = (
        "id_agente",
        "dni",
        "nombre_apellido",
        "contacto",
        "email",
    )
    list_filter = ("id_especialidad",)
    search_fields = ("nombre_apellido", "email", "dni")
