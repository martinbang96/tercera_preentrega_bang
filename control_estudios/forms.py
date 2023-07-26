from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    comision = forms.IntegerField(required=True, max_value=50000)

class EstudianteFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256)
    dni = forms.CharField(max_length=32)

class ProfesorFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256)
    dni = forms.CharField(max_length=32)
    profesion = forms.CharField(max_length=128)