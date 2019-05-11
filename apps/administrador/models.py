from django.db import models
from apps.odontologia.models import Dentista
from apps.paciente.models import Comuna, Sexo
from apps.empleado.models import Producto



class TipoServicio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre :',max_length = 50, blank = False, null = False)
    estado = models.BooleanField('Estado :', default = True)

    class Meta:
        verbose_name = 'TipoServicio'
        verbose_name_plural = 'TipoServicios'

    def __str__(self):
        return self.nombre    



class TipoCargo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre :',max_length = 50, blank = False, null = False)
    estado = models.BooleanField('Estado :', default = True)

    class Meta:
        verbose_name = 'TipoCargo'
        verbose_name_plural = 'TipoCargos'

    def __str__(self):
        return self.nombre 


class Empleado(models.Model):
    rut = models.CharField('Rut :', primary_key = True, max_length = 12, blank = False, null = False)
    nombre = models.CharField('Nombre :',max_length = 50, blank = False, null = False)
    appaterno = models.CharField('Apellido Paterno :',max_length = 50, blank = False, null = False)
    apmaterno= models.CharField('Apellido Materno :',max_length = 50, blank = False, null = False)
    id_sexo = models.ForeignKey(Sexo, on_delete = models.CASCADE)
    fono = models.IntegerField('Telefono :',blank = False, null = False)
    email = models.EmailField('Email :',blank = False, null = False)
    direccion = models.CharField('Dirección :',max_length = 100, blank = False, null = False)
    id_comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE)
    f_contrato= models.DateField('Fecha de Contrato :',blank = False, null = False)
    salario = models.IntegerField('Salario :',blank = False, null = False)
    id_tipo_cargo = models.ForeignKey(TipoCargo, on_delete = models.CASCADE)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Empleado' 
        verbose_name_plural = 'Empleados'    


    def __str__(self):
        return self.nombre

      
class Servicio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre :',max_length = 200, blank = False, null = False)
    descripcion = models.CharField('Descripción :',max_length = 200, blank = False, null = False)
    costo = models.IntegerField('Costo :', blank = False, null = False)
    id_tipo_servicio = models.ForeignKey(TipoServicio, on_delete = models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    estado = models.BooleanField('Estado', default = True)
    

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombre         




# Create your models here.
