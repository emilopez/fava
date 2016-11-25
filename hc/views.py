from django.shortcuts import render
from .models import Paciente, Profesional

# Create your views here.
def pacientes(request):
    pacientes = Paciente.objects.order_by('apellido')
    #Question.objects.order_by('-pub_date')[:5]
    return render(request, 'hc/pacientes.html', {'pacientes': pacientes})
