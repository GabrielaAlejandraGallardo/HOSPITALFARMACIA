from django.contrib import admin

from .models import (
    Medicamento,
    Estado_medicamento,
    Nivel_Riesgo,
    Refrigeracion,
    Laboratorio,
)

admin.site.register(Medicamento)
admin.site.register(Estado_medicamento)
admin.site.register(Nivel_Riesgo)
admin.site.register(Refrigeracion)
admin.site.register(Laboratorio)


