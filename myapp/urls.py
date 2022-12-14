from django.urls import path
from myapp.views import Familiar_view, Mascota_view, Vehiculo_view, BuscarFamiliar, ActualizarFamiliar, BorrarFamiliar, BuscarVehiculo, BuscarMascota, ActualizarVehiculo, BorrarVehiculo, ActualizarMascota, BorrarMascota


urlpatterns = [
    path('mi-familia/', Familiar_view.autogenerar_listar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
   
    path('mi-vehiculo/', Vehiculo_view.autogenerar_listar_vehiculos),
    path('mi-vehiculo/buscar', BuscarVehiculo.as_view()),
    path('mi-vehiculo/actualizar/<int:pk>', ActualizarVehiculo.as_view()),
    path('mi-vehiculo/borrar/<int:pk>', BorrarVehiculo.as_view()),
    
    path('mi-mascota/', Mascota_view.autogenerar_listar_mascotas),
    path('mi-mascota/buscar', BuscarMascota.as_view()),
    path('mi-mascota/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mi-mascota/borrar/<int:pk>', BorrarMascota.as_view()),







    ]
