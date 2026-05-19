from django.contrib import admin

# Register your models here.
from .models import Agente, Especialidad

admin.site.register(Agente)
admin.site.register(Especialidad)