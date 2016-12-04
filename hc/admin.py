from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paciente, Profesional, Consulta, Adjunto, HistoriaClinica, Antecedente, TipoAntecedente, HcAntDetalle

admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Consulta)
admin.site.register(Adjunto)
admin.site.register(HistoriaClinica)
admin.site.register(Antecedente)
admin.site.register(TipoAntecedente)
admin.site.register(HcAntDetalle)
