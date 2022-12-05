from django.urls import path
from .vistas import Saludo_view, Familiar_view

urlpatterns = [
    path('saludo', Saludo_view.saludo),
    path('autogenerar_listar_familiares', Familiar_view.autogenerar_listar_familiares)
    ]
