from django.urls import path
from .views import crearPaciente, editarPaciente, crearReservacion, listarReservacion, editarReservacion, eliminarReservacion



urlpatterns =[
    path('crear_paciente/',crearPaciente, name = 'crear_paciente'),
    path('editar_paciente/<rut>',editarPaciente, name = 'editar_paciente'),
    path('crear_reservacion/',crearReservacion, name = 'crear_reservacion'),
    path('listar_reservacion/',listarReservacion, name = 'listar_reservacion'),
    path('editar_reservacion/<int:id>',editarReservacion, name = 'editar_reservacion'),
    path('eliminar_reservacion/<int:id>',eliminarReservacion, name = 'eliminar_reservacion'),
]