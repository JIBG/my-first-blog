from django import forms
from .models import Paciente, Reservacion, Comuna, Sexo
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.forms.fields import DateField


class PacienteForm(forms.ModelForm):
     class Meta:
         model = Paciente
         fields = ['rut','nombre','appaterno','apmaterno','fecha_nacimiento','fono','email','direccion','id_comuna','id_sexo']
         widgets = {
         'rut': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Ingresar Rut', 'type':'text'}),
         'nombre': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Ingresar Nombre', 'type':'text'}),
         'appaterno': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Ingresar Apellido Paterno', 'type':'text'}),
         'apmaterno': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Ingresar Apellido Materno', 'type':'text'}),
         'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha de Nacimiento', 'type':'date'}),
         'fono': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Ingresar Fono', 'type':'text'}),
         'email': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Ingresar Email', 'type':'text'}),
         'direccion': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Ingresar Direccion', 'type':'text'}),
         'id_comuna': forms.Select( attrs={'class':'form-control', 'placeholder':'Seleccionar Comuna', 'type':'text'}),
         'id_sexo': forms.Select( attrs={'class':'form-control', 'placeholder':'Seleccionar Sexo', 'type':'text'})

         }
         labels = {
         'id_comuna':'Comuna',
         'id_sexo':'Sexo'    


         }
         

class ReservacionForm(forms.ModelForm):
    class Meta:
         model = Reservacion
         fields = ['fecha','hora', 'id_paciente','id_dentista','id_servicio']
         widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha a Reservar', 'type':'date'}),
        'hora': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Seleccionar Hora', 'type':'time'}),
        'id_paciente': forms.Select( attrs={'class':'form-control', 'placeholder':'Seleccionar Paciente', 'type':'text'}),
        'id_dentista': forms.Select( attrs={'class':'form-control', 'placeholder':'Seleccionar Dentista', 'type':'text'}),
        'id_servicio': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Seleccionar Servicio', 'type':'text'})
          }
         labels = {
        'id_paciente' : 'Paciente',
        'id_dentista' : 'Dentista',
        'id_servicio' : 'Servicio'

         }
         
           

class Comuna(forms.ModelForm):
     class Meta:
         model = Comuna
         fields = '__all__'   

class Sexo(forms.ModelForm):
     class Meta:
         model = Sexo
         fields = '__all__'   