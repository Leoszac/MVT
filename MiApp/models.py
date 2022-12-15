from django.db import models

class escuela(models.Model):
    taller = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 100)
    
class profesor(models.Model):
    nombre = models.CharField(max_length = 100)
    taller = models.CharField(max_length = 100)
    DNI = models.IntegerField()


class alumno(models.Model):
    deporte = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 100)
    DNI = models.IntegerField()
    
    
    