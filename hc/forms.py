from django import forms
from .models import Paciente, Profesional, Consulta
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('apellido', 'nombre','documento','fecha_nacimiento', 'nacionalidad', 'estado_civil', 'sexo', 'ocupacion','domicilio','telefono','obra_social','email',)
        widgets = {
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'obra_social': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfesionalForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'last_name', 'first_name',  )

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ('entrada',)
        labels = {
            'entrada': _(''),
        }
        widgets = {
            'entrada': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
        }
