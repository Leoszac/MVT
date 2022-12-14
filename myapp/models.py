from django.db import models
import datetime

# Create your models here.
# class Familiar(models.Model):
    
#     nombre = models.CharField(max_length=100)
#     direccion = models.CharField(max_length=200)
#     numero_pasaporte = models.IntegerField()
    
#     def __str__(self):
#       return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"


class Familiar(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField (max_length=100,null=False)
    edad = models.IntegerField(null=False)
    fecha_nacimiento = models.DateField(null=False)

    def __init__(self, nombre: str, edad: int, fecha_nacimiento: datetime.date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento

class Mascota(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(null=False)


    def __init__(self, nombre: str, edad: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.edad = edad

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

