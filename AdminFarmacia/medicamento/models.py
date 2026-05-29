from django.db import models
from deposito.models import *

class Laboratorio(models.Model):
    id_laboratorio=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Estado_medicamento(models.Model):
    id_estado=models.IntegerField(primary_key=True)
    descripcion=models.TextField(max_length=200)
    
class Nivel_Riesgo(models.Model):
    id_nivel_de_riesgo=models.AutoField(primary_key=True)
    descripcion=models.TextField(max_length=200)
        

class Medicamento(models.Model):
    id_medicamento=models.AutoField(primary_key=True)
    description=models.TextField(max_length=200)
    laboratorios = models.ManyToManyField(Laboratorio)
    fecha_vencimiento=models.DateField()
    lote=models.TextField(max_length=200)
    fecha_ingreso=models.DateField()
    id_deposito=models.ForeignKey(Deposito,on_delete=models.CASCADE)
    fecha_dispensa=models.DateField()
    qr=models.ImageField(upload_to='medicamento/qr/', blank=True, null=True, verbose_name="QR")
    cod_barra=models.IntegerField()
    id_estado=models.ForeignKey(Estado_medicamento,on_delete=models.CASCADE)
    refrigeracion=models.TextField(max_length=30)
    id_nivel_de_riesgo = models.ForeignKey(
        Nivel_Riesgo,
        related_name='riesgo_medicamento',
        on_delete=models.CASCADE,
        max_length=20,
    )
    cant_stock=models.IntegerField()


 