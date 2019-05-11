from django.contrib import admin
from .models import Paciente, Reservacion, Comuna, Sexo
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Reservacion)
admin.site.register(Comuna)
admin.site.register(Sexo)