from django.db import models
<<<<<<< HEAD
from deposito.models import Deposito

from django.db import models

from .models import *
=======
from deposito.models import *

>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89

class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


<<<<<<< HEAD
class Estado_medicamento(models.Model):
=======
class Estado_descartable(models.Model):
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
    id_estado = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=200)


class Nivel_Riesgo(models.Model):
    id_nivel_de_riesgo = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=200)


class Refrigeracion(models.Model):
    refrigeracion = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=200)

<<<<<<< HEAD
class Descartable(models.Model):
    id_descartable = models.AutoField(primary_key=True)
    description = models.TextField(max_length=200)

=======

class Descartable(models.Model):
    id_descartable = models.AutoField(primary_key=True)
    description = models.TextField(max_length=200)
    # Django expects medicamento_medicamento.id_laboratorio_id to exist.
    # Your current DB table does not have that column; making it optional
    # prevents migrations/ORM from forcing NOT NULL during schema repair.
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
    id_laboratorio = models.ForeignKey(
        Laboratorio, on_delete=models.CASCADE, null=True, blank=True
    )
    fecha_vencimiento = models.DateField()
    lote = models.TextField(max_length=200)
    fecha_ingreso = models.DateField()
<<<<<<< HEAD

    id_deposito = models.ForeignKey(
        Deposito,
        on_delete=models.CASCADE,
        related_name="descartables",
    )

    fecha_dispensa = models.DateField(null=True, blank=True)

    qr = models.ImageField(
        upload_to="descartable/qr/", blank=True, null=True, verbose_name="QR"
    )

    cod_barra = models.IntegerField()

    id_estado = models.ForeignKey(Estado_medicamento, on_delete=models.CASCADE)

    refrigeracion = models.ForeignKey(
        Refrigeracion, on_delete=models.CASCADE, max_length=20
    )

    id_nivel_de_riesgo = models.ForeignKey(
        Nivel_Riesgo,
        related_name="riesgo",
        on_delete=models.CASCADE,
        max_length=20,
    )

    cant_stock = models.IntegerField()


class Dispensa_descartable(models.Model):
=======
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
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
    id_dispensa = models.AutoField(primary_key=True)
    id_descartable = models.ForeignKey(
        Descartable, on_delete=models.CASCADE, related_name="dispensas"
    )
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return (
            f"Dispensa_descartable{self.id_dispensa} - "
            f"{self.id_descartable.description} ({self.cantidad})"
        )

=======
        return f"Dispensa {self.id_dispensa} - {self.id_descartable.description} ({self.cantidad})"
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
