from django.contrib import admin

from .models import Descartable, Dispensa, Estado_descartable, Laboratorio, Nivel_Riesgo, Refrigeracion

admin.site.register(Descartable)
admin.site.register(Estado_descartable)
admin.site.register(Nivel_Riesgo)
admin.site.register(Refrigeracion)
admin.site.register(Laboratorio)
admin.site.register(Dispensa)

