from django.urls import path
from apps.odontologia.views import crearDentista, listarDentista, editarDentista, eliminarDentista, crearReserva
from .views import crearServicio, editarServicio, listarServicio, eliminarServicio, listarPaciente, eliminarPaciente, crearEmpleado, listarEmpleado, eliminarEmpleado




urlpatterns =[
    path('crear_dentista/',crearDentista, name = 'crear_dentista'),
    path('listar_dentista/',listarDentista, name = 'listar_dentista'),
    path('editar_dentista/<int:rut>',editarDentista, name = 'editar_dentista'),
    path('eliminar_dentista/<int:rut>',eliminarDentista, name = 'eliminar_dentista'),
    path('crear_reserva/',crearReserva, name = 'crear_reserva'),

    path('listar_paciente/',listarPaciente, name = 'listar_paciente'),
    path('eliminar_paciente/<rut>',eliminarPaciente, name = 'eliminar_paciente'),
    path('crear_servicio/',crearServicio, name = 'crear_servicio'),
    path('editar_servicio/<int:id>',editarServicio, name = 'editar_servicio'),
    path('listar_servicio/',listarServicio, name = 'listar_servicio'),
    path('eliminar_servicio/<int:id>',eliminarServicio, name = 'eliminar_servicio'),
    path('crear_empleado/',crearEmpleado, name = 'crear_empleado'),
    path('listar_empleado/',listarEmpleado, name = 'listar_empleado'),
    path('eliminar_empleado/<rut>',eliminarEmpleado, name = 'eliminar_empleado'),
]