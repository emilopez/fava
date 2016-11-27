from django.shortcuts import render, get_object_or_404
from .models import Paciente, Profesional

# Create your views here.
def pacientes(request):
    pacientes = Paciente.objects.order_by('apellido')
    #Question.objects.order_by('-pub_date')[:5]
    return render(request, 'hc/pacientes.html', {'pacientes': pacientes})

def paciente_detalle(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'hc/paciente.html', {'paciente': paciente})
