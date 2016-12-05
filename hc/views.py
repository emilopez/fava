from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Profesional, Antecedente, TipoAntecedente
from .forms import PacienteForm, ConsultaForm, AntecedenteForm, TipoAntecedenteForm

@login_required
def pacientes(request):
    pacientes = Paciente.objects.order_by('apellido')
    return render(request, 'hc/pacientes.html', {'pacientes': pacientes})

@login_required
def paciente_detalle(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente
            consulta.save()
    else:
        form = ConsultaForm()
    return render(request, 'hc/paciente.html', {'paciente': paciente, 'form': form})

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

@login_required
def paciente_eliminar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('pacientes')

@login_required
def antecedentes(request):
    antecedentes = Antecedente.objects.order_by('tipo')
    return render(request, 'hc/antecedentes.html', {'antecedentes': antecedentes})

@login_required
def antecedente_nuevo(request):
    if request.method == "POST":
        form = AntecedenteForm(request.POST)
        if form.is_valid():
            antecedente = form.save(commit=False)
            antecedente.save()
            return redirect('antecedentes')
    else:
        form = AntecedenteForm()
    return render(request, 'hc/antecedente_editar.html', {'form': form})

@login_required
def tipo_antecedente_listar(request):
    tipos_antecedente = TipoAntecedente.objects.order_by('texto')
    if request.method == "POST":
        form = TipoAntecedenteForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect('tipo_antecedente_listar')
    else:
        form = TipoAntecedenteForm()
    return render(request, 'hc/tipo_antecedente_listar.html', {'tipos_antecedente': tipos_antecedente, 'form':form})
