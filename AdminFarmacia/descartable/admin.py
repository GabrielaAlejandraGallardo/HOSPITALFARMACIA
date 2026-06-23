from django.contrib import admin

<<<<<<< HEAD
from .models import Descartable, Dispensa_descartable,Estado_medicamento,Nivel_Riesgo,Refrigeracion,Laboratorio


admin.site.register(Descartable)
admin.site.register(Estado_medicamento)
admin.site.register(Nivel_Riesgo)
admin.site.register(Refrigeracion)
admin.site.register(Laboratorio)
admin.site.register(Dispensa_descartable)
=======
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
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
