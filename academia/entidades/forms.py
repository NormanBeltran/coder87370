from django import forms
from .models import *

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del Curso")
    comision = forms.IntegerField(label="Número de Comisión", required=True)
    profesor = forms.ModelChoiceField(queryset=Profesor.objects.all(), label="Profesor", required=False)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=60, label="Nombre")
    apellido = forms.CharField(max_length=60, label="Apellido")
    email = forms.EmailField(label="Email")
    profesion = forms.CharField(max_length=50, label="Profesión")