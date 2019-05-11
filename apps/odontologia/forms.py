from django import forms
from .models import Dentista, Reserva

class DentistaForm(forms.ModelForm):
     class Meta:
         model = Dentista
         fields = ['rut','nombre','apellido','descripcion']


class ReservaForm(forms.ModelForm):
     class Meta:
         model = Reserva
         fields = ['id','titulo','fecha','autor_id']         