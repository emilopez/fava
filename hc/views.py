from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Profesional
from .forms import PacienteForm

@login_required
def pacientes(request):
    pacientes = Paciente.objects.order_by('apellido')
    #Question.objects.order_by('-pub_date')[:5]
    return render(request, 'hc/pacientes.html', {'pacientes': pacientes})

@login_required
def paciente_detalle(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'hc/paciente.html', {'paciente': paciente})

@login_required
def paciente_nuevo(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.medico = request.user
            paciente.save()
            return redirect('paciente_detalle', pk=paciente.pk)
    else:
        form = PacienteForm()
    return render(request, 'hc/paciente_editar.html', {'form': form})

@login_required
def paciente_editar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.medico = request.user
            paciente.save()
            return redirect('paciente_detalle', pk=paciente.pk)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'hc/paciente_editar.html', {'form': form})
