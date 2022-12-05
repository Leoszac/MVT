from django.db import models
import datetime

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
