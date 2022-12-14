from django.db import models
import datetime

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fecha_compra = models.DateField()
    kilometraje = models.FloatField(default=0.0)


    def __init__(self, marca: str, modelo: str, kilometraje: int,fecha_compra: datetime.date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marca = marca
        self.modelo = modelo
        self.fecha_compra = fecha_compra
        self.kilometraje = kilometraje
