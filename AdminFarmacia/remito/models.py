from django.db import models
from deposito.models import Deposito
from medicamento.models import Medicamento
from descartable.models import Descartable


class Remito(models.Model):
    id_remito = models.AutoField(primary_key=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    id_deposito_origen = models.ForeignKey(
        Deposito,
        on_delete=models.CASCADE,
        related_name="remitos_origen"
    )
    id_deposito_destino = models.ForeignKey(
        Deposito,
        on_delete=models.CASCADE,
        related_name="remitos_destino"
    )
    observaciones = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Remito {self.id_remito} — {self.id_deposito_origen} → {self.id_deposito_destino}"


class RemitoMedicamento(models.Model):
    id_remito_medicamento = models.AutoField(primary_key=True)
    id_remito = models.ForeignKey(
        Remito,
        on_delete=models.CASCADE,
        related_name="items_medicamentos"
    )
    id_medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE,
        related_name="remitos"
    )
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.id_medicamento.description} x{self.cantidad} (Remito {self.id_remito.id_remito})"


class RemitoDescartable(models.Model):
    id_remito_descartable = models.AutoField(primary_key=True)
    id_remito = models.ForeignKey(
        Remito,
        on_delete=models.CASCADE,
        related_name="items_descartables"
    )
    id_descartable = models.ForeignKey(
        Descartable,
        on_delete=models.CASCADE,
        related_name="remitos"
    )
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.id_descartable.description} x{self.cantidad} (Remito {self.id_remito.id_remito})"

