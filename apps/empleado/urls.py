from django.urls import path
from .views import editarEmpleado, crearProducto, editarProducto, listarProducto, eliminarProducto, crearAtencion, listarAtencion, eliminarAtencion




urlpatterns =[

    path('editar_empleado/<rut>',editarEmpleado, name = 'editar_empleado'),
    path('crear_producto/',crearProducto, name = 'crear_producto'),
    path('editar_producto/<int:id>',editarProducto, name = 'editar_producto'),
    path('listar_producto/',listarProducto, name = 'listar_producto'),
    path('eliminar_producto/<int:id>',eliminarProducto, name = 'eliminar_producto'),
    path('crear_atencion/',crearAtencion, name = 'crear_atencion'),
    path('listar_atencion/',listarAtencion, name = 'listar_atencion'),
    path('eliminar_atencion/<int:id>',eliminarAtencion, name = 'eliminar_atencion'),
]