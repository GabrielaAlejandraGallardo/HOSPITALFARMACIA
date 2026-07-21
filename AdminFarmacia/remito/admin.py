from django.contrib import admin
from .models import Remito, RemitoMedicamento, RemitoDescartable


class RemitoMedicamentoInline(admin.TabularInline):
    model = RemitoMedicamento
    extra = 1


class RemitoDescartableInline(admin.TabularInline):
    model = RemitoDescartable
    extra = 1


class RemitoAdmin(admin.ModelAdmin):
    inlines = [RemitoMedicamentoInline, RemitoDescartableInline]
    list_display = ("id_remito", "fecha_emision", "id_deposito_origen", "id_deposito_destino")
    list_filter = ("fecha_emision", "id_deposito_origen", "id_deposito_destino")


admin.site.register(Remito, RemitoAdmin)
admin.site.register(RemitoMedicamento)
admin.site.register(RemitoDescartable)
