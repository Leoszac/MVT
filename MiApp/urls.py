from django.urls import path
from MiApp.views import index, nuevo_taller, nuevo_profesor, nuevo_alumno, buscar_profesor, buscar_escuela
from .forms import escuelaForm, profesorForm, alumnoForm


urlpatterns = [
    path('', index),
    path('nuevo_taller/', nuevo_taller),
    path('nuevo_profesor/', nuevo_profesor),
    path('nuevo_alumno/', nuevo_alumno),
    path('buscar_escuela/', buscar_escuela),
    path('buscar_profesor/', buscar_profesor),
    path('escuelaForm/', escuelaForm),
    path('profesorForm/', profesorForm),
    path('alumnoForm/', alumnoForm),]
