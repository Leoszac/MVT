from django.db import models
import datetime

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(null=False)


    def __init__(self, nombre: str, edad: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.edad = edad
