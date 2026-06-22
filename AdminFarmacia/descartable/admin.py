from django.contrib import admin

# Register your models here.
from .models import (
    Descartable,
    Laboratorio,
    Estado_descartable,
    Nivel_Riesgo,
    Refrigeracion,
    Dispensa,
)


admin.site.register(Estado_descartable)
admin.site.register(Nivel_Riesgo)
admin.site.register(Laboratorio)
admin.site.register(Refrigeracion)
admin.site.register(Descartable)
admin.site.register(Dispensa)
