from django.contrib import admin

from .models import Descartable, Dispensa_descartable,Estado_medicamento,Nivel_Riesgo,Refrigeracion,Laboratorio


admin.site.register(Descartable)
admin.site.register(Estado_medicamento)
admin.site.register(Nivel_Riesgo)
admin.site.register(Refrigeracion)
admin.site.register(Laboratorio)
admin.site.register(Dispensa_descartable)