from django.db import models

# Create your models here.
class Dentista(models.Model):
    rut = models.IntegerField(primary_key = True, blank = False, null = False)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellido = models.CharField(max_length = 200, blank = False, null = False)
    descripcion = models.TextField('Descripción :', blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Dentista' 
        verbose_name_plural = 'Dentistas'    


    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 255, blank = False, null = False)
    fecha = models.DateField('Fecha de Reserva', blank = False, null = False)
    autor_id = models.ForeignKey(Dentista, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return self.titulo    