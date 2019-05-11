from django import forms
from .models import Servicio, TipoServicio, Empleado, TipoCargo
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class ServicioForm(forms.ModelForm):
     class Meta:
         model = Servicio
         fields = ['nombre', 'descripcion','costo','id_empleado','id_tipo_servicio','id_producto']
         widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre', 'type':'text'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Descripcion', 'type':'text'}),
            'costo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Costo', 'type':'text'}),
            'id_empleado': forms.Select(attrs={'class':'form-control','placeholder':'Seleccionar Empleado', 'type':'text'}),
            'id_tipo_servicio': forms.Select(attrs={'class':'form-control','placeholder':'Seleccionar Tipo de Servicio', 'type':'text'}),
            'id_producto': forms.Select(attrs={'class':'form-control','placeholder':'Seleccionar Producto', 'type':'text'}),
        
          }   


class TipoServicio(forms.ModelForm):
     class Meta:
         model = TipoServicio
         fields = '__all__' 


class EmpleadoForm(forms.ModelForm):
     class Meta:
         model = Empleado
         fields = ['rut','nombre','appaterno','apmaterno','id_sexo','fono','email','direccion','id_comuna','f_contrato','salario','id_tipo_cargo', 'estado'] 
         widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Rut', 'type':'text'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre', 'type':'text'}),
            'appaterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Apellido Paterno', 'type':'text'}),
            'apmaterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Apellido Materno', 'type':'text'}),
            'id_sexo': forms.Select(attrs={'class':'form-control','placeholder':'Seleccionar Sexo', 'type':'text'}),
            'fono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Telefono', 'type':'text'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Email', 'type':'text'}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Direccion', 'type':'text'}),
            'id_comuna': forms.Select(attrs={'class':'form-control','placeholder':'Seleccionar Comuna', 'type':'text'}),
            'f_contrato': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha de Contrato', 'type':'date'}),
            'salario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Salario', 'type':'text'}),
            'id_tipo_cargo': forms.Select(attrs={'class':'form-control','placeholder':'Seleccionar Tipo de Cargo', 'type':'text'})
            
        
          }  

class TipoCargo(forms.ModelForm):
     class Meta:
         model = TipoCargo
         fields = '__all__' 
