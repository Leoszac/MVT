from django.shortcuts import render, get_object_or_404
from myapp.modelos import Familiar, Mascota, Vehiculo
from formularios.forms import BuscarMascotaForm, BuscarPersonasForm, BuscarVehiculoForm, PersonaForm, VehiculoForm, MascotaForm, ActualizarMascotaForm, ActualizarPersonaForm, ActualizarVehiculoForm
import datetime
from django.views import View

class Familiar_view:

    def autogenerar_listar_familiares(request):
        fm1 = Familiar("Juan", 30, datetime.date(1992, 12, 3))
        fm2 = Familiar("Nicolas", 36, datetime.date(1986, 5, 12))
        fm3 = Familiar("Pedro", 20, datetime.date(2002, 5, 10))
        fm1.save()
        fm2.save()
        fm3.save()

        return render(request,'autogenerar_listar_familiares.html', {"familiares": [fm1, fm2, fm3]} )




def index(request):
    return render(request, "/index.html")

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "/listar-familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):
    form_class = BuscarPersonasForm
    template_name = '/buscar-personas.html'
    initial = {"nombre":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
  form_class = PersonaForm
  template_name = '/actualizar-familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarFamiliar(View):
  template_name = '/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})




class Vehiculo_view:

    def autogenerar_listar_vehiculos(request):
        fm6 = Vehiculo("Fiat", "Palio", 180000 ,datetime.date(2002, 5, 10))
        fm7 = Vehiculo("Renault", "Logan", 18751 ,datetime.date(2022, 5, 10))
        fm6.save()
        fm7.save()

        return render(request,'autogenerar_listar_vehiculos.html', {"Vehiculos": [fm6, fm7]} )


def mostrar_vehiculo(request):
  lista_vehiculos = Vehiculo.objects.all()
  return render(request, "/listar-vehiculos.html", {"lista_vehiculos": lista_vehiculos})


class BuscarVehiculo(View):
    form_class = BuscarVehiculoForm
    template_name = '/buscar-vehiculo.html'
    initial = {"marca":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_vehiculos = Vehiculo.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_vehiculos':lista_vehiculos})
        return render(request, self.template_name, {"form": form})


class ActualizarVehiculo(View):
  form_class = VehiculoForm
  template_name = '/actualizar-vehiculo.html'
  initial = {"marca":"", "modelo":"", "fecha_compra":"", "kilometraje":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      vehiculo = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=vehiculo)
      return render(request, self.template_name, {'form':form,'vehiculo': vehiculo})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      vehiculo = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=vehiculo)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el vehiculo {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'vehiculo': vehiculo,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarVehiculo(View):
  template_name = '/listar-vehiculos.html'
  
  def get(self, request, pk): 
      vehiculo = get_object_or_404(Familiar, pk=pk)
      vehiculo.delete()
      vehiculos = Familiar.objects.all()
      return render(request, self.template_name, {'lista_vehiculos': vehiculos})


def mostar_mascota(request):
  lista_mascotas = Mascota.objects.all()
  return render(request, "/listar-masctoas.html", {"lista_vehiculos": lista_mascotas})


class BuscarMascota(View):
    form_class = BuscarMascotaForm
    template_name = '/buscar-mascota.html'
    initial = {"nombre":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Vehiculo.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})





class Mascota_view:

    def autogenerar_listar_mascotas(request):
        fm4 = Mascota("Firulais", 5,)
        fm5 = Mascota("Rinoceronte", 3)
        fm4.save()
        fm5.save()

        return render(request,'autogenerar_listar_mascotas.html', {"Mascotas": [fm4, fm5]} )


class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = '/actualizar-mascota.html'
  initial = {"nombre":"", "edad":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      mascota = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      mascota = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarMascota(View):
  template_name = '/listar-vehiculos.html'
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Familiar, pk=pk)
      mascota.delete()
      mascotas = Familiar.objects.all()
      return render(request, self.template_name, {'lista_mascota': mascota})