from django import forms
from .models import Producto, Atencion
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class ProductoForm(forms.ModelForm):
     class Meta:
         model = Producto
         fields = ['nombre', 'descripcion','unimed','precos','preven']


class AtencionForm(forms.ModelForm):
     class Meta:
         model = Atencion
         fields = ['fecha','id_dentista', 'id_paciente']     
         widgets = {
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha de Atencion', 'type':'date'}),
        
          }    