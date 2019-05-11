from django.urls import path
from .views import crearDentista, listarDentista, editarDentista, eliminarDentista, crearReserva



urlpatterns =[
    path('crear_dentista/',crearDentista, name = 'crear_dentista'),
    path('listar_dentista/',listarDentista, name = 'listar_dentista'),
    path('editar_dentista/<int:rut>',editarDentista, name = 'editar_dentista'),
    path('eliminar_dentista/<int:rut>',eliminarDentista, name = 'eliminar_dentista'),
    path('crear_reserva/',crearReserva, name = 'crear_reserva'),
]