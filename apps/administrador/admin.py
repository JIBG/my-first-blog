from django.contrib import admin
from .models import Servicio, TipoServicio, Empleado, TipoCargo
# Register your models here.
admin.site.register(Servicio)
admin.site.register(TipoServicio)
admin.site.register(Empleado)
admin.site.register(TipoCargo)

