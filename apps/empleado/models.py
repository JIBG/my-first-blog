from django.db import models
from apps.paciente.models import Paciente
from apps.odontologia.models import Dentista

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre :',max_length = 200, blank = False, null = False)
    descripcion = models.CharField('Descripción :',max_length = 200)
    unimed = models.IntegerField('Unidad de Medida :', blank = False, null = False)
    precos = models.IntegerField('Precio Costo :', blank = False, null = False)
    preven = models.IntegerField('Precio Venta :', blank = False, null = False)
    id_producto_servicio = models.CharField('Producto Servicio :',max_length = 50, blank = False, null = False)
    estado = models.BooleanField('Estado :', default = True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre 

class Atencion(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField('Fecha Atención :')
    id_dentista = models.ForeignKey(Dentista, on_delete = models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE)
    estado = models.BooleanField('Estado :', default = True)

    class Meta:
        verbose_name = 'Atencion'
        verbose_name_plural = 'Atenciones'

    def __str__(self):
        return self.nombre         