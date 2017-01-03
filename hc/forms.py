from django import forms
from .models import Paciente, Profesional, Consulta, TipoAntecedente, Antecedente, Estudio, Parametro
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('apellido', 'nombre','obra_social','codigo_obra_social', 'documento','fecha_nacimiento', 'lugar_nacimiento', 'estado_civil', 'sexo', 'ocupacion','domicilio','telefono','email',)
        labels = {
            'codigo_obra_social': _('Código obra social'),
            'fecha_nacimiento':_('Fecha de nacimiento (dd/mm/aaaa)'),
            'lugar_nacimiento':_('Lugar de nacimiento'),
        }
        widgets = {
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'lugar_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'obra_social': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_obra_social': forms.TextInput(attrs={'class': 'form-control', 'label':'Código obra social'}),
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
            'entrada': _(''), # para cambiar la etiqueta
        }
        widgets = {
            'entrada': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
        }

class AntecedenteForm(forms.ModelForm):
    class Meta:
        model = Antecedente
        fields = ('tipo', 'texto', )
        labels = {
            'tipo': _('Clasificación'), # para cambiar la etiqueta
            'texto': _('Tipo'),
        }
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'texto': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoAntecedenteForm(forms.ModelForm):
    class Meta:
        model = TipoAntecedente
        fields = ('texto', )
        labels = {'texto': _('Clasificación'), }# para cambiar la etiqueta
        widgets = {'texto': forms.TextInput(attrs={'class': 'form-control'}), }

class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = ('texto', )
        labels = {'texto': _('Nombre del estudio'),}
        widgets = {'texto': forms.TextInput(attrs={'class': 'form-control'}),}

class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = ('estudio','texto', )
        labels = {'texto': _('Parámetro'),}
        widgets = {
            'estudio': forms.Select(attrs={'class': 'form-control'}),
            'texto': forms.TextInput(attrs={'class': 'form-control'}),
        }
