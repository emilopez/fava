from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Profesional, Antecedente, TipoAntecedente, Estudio, Parametro, Resultado
from .forms import PacienteForm, ConsultaForm, AntecedenteForm, TipoAntecedenteForm, EstudioForm, ParametroForm, HistoricoForm
# , ResultadoForm

from datetime import date

@login_required
def pacientes(request):
    pacientes = Paciente.objects.order_by('apellido')
    for p in pacientes:
        p.set_edad()
    return render(request, 'hc/pacientes.html', {'pacientes': pacientes})

@login_required
def paciente_detalle(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
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

@login_required
def estudio_nuevo(request):
    estudios = Estudio.objects.order_by('texto')
    if request.method == "POST":
        if 'guardarestudio' in request.POST:
            form = EstudioForm(request.POST)
        elif 'guardarparametro' in request.POST:
            form = ParametroForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
        return redirect('estudio_nuevo')
    else:
        form_estudio = EstudioForm()
        form_parametro = ParametroForm()
    return render(request, 'hc/estudio_listar.html', {'estudios':estudios, 'form_estudio':form_estudio, 'form_parametro':form_parametro})

@login_required
def estudio_eliminar(request, pk):
    estudio = get_object_or_404(Estudio, pk=pk)
    estudio.delete()
    return redirect('estudio_nuevo')

@login_required
def parametro_eliminar(request, pk):
    parametro = get_object_or_404(Parametro, pk=pk)
    parametro.delete()
    return redirect('estudio_nuevo')

@login_required
def hc_editar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    if request.method == "POST":
        if 'nueva_consulta' in request.POST:
            form_consulta = ConsultaForm(request.POST)
            if form_consulta.is_valid():
                consulta = form_consulta.save(commit=False)
                consulta.paciente = paciente
                consulta.save()
        elif 'nuevo_antecedente' in request.POST:
            form_historico_antecedente = HistoricoForm(request.POST)
            if form_historico_antecedente.is_valid():
                form_historico_antecedente = form_historico_antecedente.save(commit=False)
                form_historico_antecedente.paciente = paciente
                form_historico_antecedente.save()
        return redirect('hc_editar', pk=pk)
    else:
        form_consulta = ConsultaForm()
        form_historico_antecedente = HistoricoForm()
        # form_resultado = ResultadoForm()
    return render(request, 'hc/hc_editar.html', {'paciente': paciente, 'form_consulta':form_consulta, 'form_historico_antecedente':form_historico_antecedente})
