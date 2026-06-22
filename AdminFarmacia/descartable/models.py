from django.db import models
from deposito.models import *


class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Estado_descartable(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=200)


class Nivel_Riesgo(models.Model):
    id_nivel_de_riesgo = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=200)


class Refrigeracion(models.Model):
    refrigeracion = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=200)


class Descartable(models.Model):
    id_descartable = models.AutoField(primary_key=True)
    description = models.TextField(max_length=200)
    # Django expects medicamento_medicamento.id_laboratorio_id to exist.
    # Your current DB table does not have that column; making it optional
    # prevents migrations/ORM from forcing NOT NULL during schema repair.
    id_laboratorio = models.ForeignKey(
        Laboratorio, on_delete=models.CASCADE, null=True, blank=True
    )
    fecha_vencimiento = models.DateField()
    lote = models.TextField(max_length=200)
    fecha_ingreso = models.DateField()
    id_deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    fecha_dispensa = models.DateField()
    qr = models.ImageField(
        upload_to="descartable/qr/", blank=True, null=True, verbose_name="QR"
    )
    cod_barra = models.IntegerField()
    id_estado = models.ForeignKey(Estado_descartable, on_delete=models.CASCADE)
    refrigeracion = models.ForeignKey(
        Refrigeracion, on_delete=models.CASCADE, max_length=20
    )
    id_nivel_de_riesgo = models.ForeignKey(Nivel_Riesgo,related_name="riesgo_descartable",on_delete=models.CASCADE,max_length=20,    )
    cant_stock = models.IntegerField()


class Dispensa(models.Model):
    id_dispensa = models.AutoField(primary_key=True)
    id_descartable = models.ForeignKey(
        Descartable, on_delete=models.CASCADE, related_name="dispensas"
    )
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispensa {self.id_dispensa} - {self.id_descartable.description} ({self.cantidad})"
