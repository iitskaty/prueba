from django import forms
from ..sistema.models import Visitas

class RegistroForm(forms.ModelForm):
    class Meta:
        model=Visitas
        fields=['nombre','rut','descripcion','hora_ingreso','hora_salida']