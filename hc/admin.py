from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paciente, Profesional, Consulta, Adjunto, Antecedente, TipoAntecedente, Historico, Estudio, Parametro, Resultado, Valor

admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Consulta)
admin.site.register(Adjunto)
admin.site.register(Antecedente)
admin.site.register(TipoAntecedente)
admin.site.register(Historico)
admin.site.register(Estudio)
admin.site.register(Parametro)
admin.site.register(Resultado)
admin.site.register(Valor)
