from django.contrib import admin

# Register your models here.
from .models import Medicamento, Estado_medicamento, Nivel_Riesgo, Laboratorio  

admin.site.register(Medicamento)
admin.site.register(Estado_medicamento)
admin.site.register(Nivel_Riesgo)
admin.site.register(Laboratorio)    