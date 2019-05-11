from django.db import models
from apps.odontologia.models import Dentista






# Create your models here.


class Sexo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre :',max_length = 50, blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.nombre   

class Comuna(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre :',max_length = 50, blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'

    def __str__(self):
        return self.nombre    


class Paciente(models.Model):
    rut = models.CharField('Rut :', primary_key = True, max_length = 12, blank = False, null = False)
    nombre = models.CharField('Nombre :',max_length = 50, blank = False, null = False)
    appaterno = models.CharField('Apellido Paterno :',max_length = 50, blank = False, null = False)
    apmaterno= models.CharField('Apellido Materno :',max_length = 50, blank = False, null = False)
    fecha_nacimiento= models.DateField('Fecha de Nacimiento :',blank = False, null = False)
    fono = models.IntegerField('Telefono :',blank = False, null = False)
    email = models.EmailField('Email :',blank = False, null = False)
    direccion = models.CharField('Dirección :',max_length = 100, blank = False, null = False)
    id_comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE)
    id_sexo = models.ForeignKey(Sexo, on_delete = models.CASCADE)
    username = models.CharField('Usuario :',max_length = 20)
    password = models.CharField('Contraseña :',max_length = 20)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Paciente' 
        verbose_name_plural = 'Pacientes'    


    def __str__(self):
        return self.nombre


class Reservacion(models.Model):
    id = models.AutoField(primary_key = True)
    
    fecha = models.DateField('Fecha :',blank = False, null = False)
    hora = models.TimeField('Hora :',blank = False, null = False)
    id_paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE)
    id_dentista = models.ForeignKey(Dentista, on_delete = models.CASCADE)
    id_servicio = models.CharField('Servicio :',max_length = 100, blank = False, null = False)
    #id_servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Reservacion'
        verbose_name_plural = 'Reservaciones'

    def __str__(self):
        return self.id_paciente.nombre



