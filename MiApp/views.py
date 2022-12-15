from django.shortcuts import render
from django.http import HttpResponse
from .models import profesor, escuela, alumno
from .forms import escuelaForm, profesorForm, alumnoForm


def index(request):
   return render(request, 'index.html')

######### BUSQUEDAS ##########


def buscar_profesor(request):
   data = request.GET.get('nombre', '')

   error = ''

   if data:
      try:
         PROD = profesor.objects.get(nombre = data)
         return render(request, 'consulta_profesor.html', {'PROD':PROD, 'nombre':data})
      except Exception as exc:
         error = 'no hay resultados'
   return render(request, 'consulta_profesor.html', {'error':error})


def buscar_escuela(request):
   data = request.GET.get('taller', '')

   error = ''

   if data:
      try:
         escuela = escuela.objects.get(deporte = data)
         return render(request, 'consulta_deporte.html', {'escuela':escuela, 'nombre':data})
      except Exception as exc:
         error = 'no hay resultados'
   return render(request, 'consulta_taller.html', {'error':error})


######### INGRESOS  ##########
def nuevo_taller(request):
   if request.method == 'POST':
      
      formulario_ND = escuelaForm(request.POST)
   
      if formulario_ND.is_valid():
         
         formulario_ND_limpio = formulario_ND.cleaned_data
         
         nuevo_profesor = escuela(deporte=formulario_ND_limpio['taller'], nombre=formulario_ND_limpio['nombre'])
         
         nuevo_profesor.save()
         
         return render(request, 'index.html')

   else:
      formulario_ND = escuelaForm()
      return render(request, 'nuevo_taller.html', {'formulario_ND': formulario_ND})

def nuevo_profesor(request):
   if request.method == 'POST':
      
      formulario_NP = profesorForm(request.POST)
      
      if formulario_NP.is_valid():
         
         formulario_NP_limpio = formulario_NP.cleaned_data
         
         nuevo_profesor = profesor(nombre=formulario_NP_limpio['nombre'], DNI=formulario_NP_limpio['DNI'], taller=formulario_NP_limpio['deporte'])
         
         nuevo_profesor.save()
         
         return render(request, 'index.html')

   else:
      formulario_NP = profesorForm()
      
      return render(request, 'nuevo_profesor.html', {'formulario_NP': formulario_NP})

def nuevo_alumno(request):
   if request.method == 'POST':
      
      formulario_NA = alumnoForm(request.POST)
      
      if formulario_NA.is_valid():
         
         formulario_NA_limpio = formulario_NA.cleaned_data
         
         nuevo_alumno = alumno(deporte=formulario_NA_limpio['taller'], nombre=formulario_NA_limpio['nombre'], DNI=formulario_NA_limpio['DNI'])
         
         nuevo_alumno.save()
         
         return render(request, 'index.html')

   else:
      formulario_NA = alumnoForm()
      
      return render(request, 'nuevo_alumno.html', {'formulario_NA': formulario_NA})



#consulta_profesor = profesor(deporte=['deporte'], nombre=['nombre'], DNI=['DNI'])
   
#  return render(request, 'consulta_profesor.html' ,{'profesor':[consulta_profesor]})


      