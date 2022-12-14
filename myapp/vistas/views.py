from django.shortcuts import render, get_object_or_404
from myapp.modelos import Familiar, Mascota, Vehiculo
from formularios.forms import BuscarMascotaForm, BuscarPersonasForm, BuscarVehiculoForm, PersonaForm, VehiculoForm, MascotaForm, ActualizarMascotaForm, ActualizarPersonaForm, ActualizarVehiculoForm
import datetime

class Familiar_view:

    def autogenerar_listar_familiares(request):
        fm1 = Familiar("Juan", 30, datetime.date(1992, 12, 3))
        fm2 = Familiar("Nicolas", 36, datetime.date(1986, 5, 12))
        fm3 = Familiar("Pedro", 20, datetime.date(2002, 5, 10))
        fm1.save()
        fm2.save()
        fm3.save()

        return render(request,'autogenerar_listar_familiares.html', {"familiares": [fm1, fm2, fm3]} )

class Mascota_view:

    def autogenerar_listar_mascotas(request):
        fm1 = Mascota("Firulais", 5,)
        fm2 = Mascota("Rinoceronte", 3)
        fm1.save()
        fm2.save()

        return render(request,'autogenerar_listar_mascotas.html', {"Mascotas": [fm1, fm2]} )


