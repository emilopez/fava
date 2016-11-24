from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paciente, Profesional, Consulta, Adjunto

admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Consulta)
admin.site.register(Adjunto)
