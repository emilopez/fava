from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Profesional, Antecedente, TipoAntecedente, Estudio, Parametro, Resultado, Consulta
from .forms import PacienteForm, ConsultaForm, AntecedenteForm, TipoAntecedenteForm, EstudioForm, ParametroForm, HistoricoForm, ResultadoForm, ValorForm
from django import forms
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
            return redirect('hc_editar', pk=paciente.pk)
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
            return redirect('hc_editar', pk=paciente.pk)
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
def hc_editar(request, pk, pk_consulta=None):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    if request.POST:
        if 'nueva_consulta' in request.POST:
            form_consulta = ConsultaForm(request.POST)
            if form_consulta.is_valid():
                consulta = form_consulta.save(commit=False)
                consulta.paciente = paciente
                consulta.save()
        elif 'nuevo_antecedente' in request.POST:
            form_historico_antecedente = HistoricoForm(request.POST)
            if form_historico_antecedente.is_valid():
                historico_antecedente = form_historico_antecedente.save(commit=False)
                historico_antecedente.paciente = paciente
                historico_antecedente.save()
        elif 'nuevo_resultado_estudio' in request.POST:
            form_resultado_estudio = ResultadoForm(request.POST)
            if form_resultado_estudio.is_valid():
                resultado_estudio = form_resultado_estudio.save(commit=False)
                resultado_estudio.paciente = paciente
                resultado_estudio.save()
        return redirect('hc_editar', pk=pk)
    else:
        form_consulta = ConsultaForm()
        form_historico_antecedente = HistoricoForm()
        form_resultado_estudio = ResultadoForm()
    return render(request, 'hc/hc_editar.html', {'paciente': paciente, 'form_consulta':form_consulta, 'form_historico_antecedente':form_historico_antecedente, 'form_resultado_estudio':form_resultado_estudio})

@login_required
def hc_consultas(request, pk, pk_consulta=None):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    if request.POST:
        form_consulta = ConsultaForm(request.POST)
        if form_consulta.is_valid():
            consulta = form_consulta.save(commit=False)
            consulta.paciente = paciente
            consulta.save()
        return redirect('hc_consultas', pk=pk)
    else:
        form_consulta = ConsultaForm()
    return render(request, 'hc/hc_consultas.html', {'paciente': paciente, 'form_consulta':form_consulta})

@login_required
def hc_antecedentes(request, pk, pk_consulta=None):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    if request.POST:
        form_historico_antecedente = HistoricoForm(request.POST)
        if form_historico_antecedente.is_valid():
            historico_antecedente = form_historico_antecedente.save(commit=False)
            historico_antecedente.paciente = paciente
            historico_antecedente.save()
        return redirect('hc_antecedentes', pk=pk)
    else:
        form_historico_antecedente = HistoricoForm()
    return render(request, 'hc/hc_antecedentes.html', {'paciente': paciente, 'form_historico_antecedente':form_historico_antecedente})

@login_required
def hc_estudios(request, pk, pk_consulta=None):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    if request.POST:
        form_resultado_estudio = ResultadoForm(request.POST)
        if form_resultado_estudio.is_valid():
            resultado_estudio = form_resultado_estudio.save(commit=False)
            resultado_estudio.paciente = paciente
            resultado_estudio.save()
        return redirect('hc_estudios', pk=pk)
    else:
        form_resultado_estudio = ResultadoForm()
    return render(request, 'hc/hc_estudios.html', {'paciente': paciente, 'form_resultado_estudio':form_resultado_estudio})

@login_required
def nuevo_valor(request, pk_resultado, pk_estudio):
    estudio = get_object_or_404(Estudio, pk=pk_estudio)
    resultado = get_object_or_404(Resultado, pk=pk_resultado)
    if request.POST:
        form = ValorForm(request.POST)
        if form.is_valid():
            valor = form.save(commit=False)
            valor.resultado = resultado
            valor.save()
        # return redirect('hc_editar', pk=resultado.paciente.pk)
        return redirect('nuevo_valor', pk_resultado, pk_estudio)
    else:
        form = ValorForm()
        form.fields['parametro'] = forms.ModelChoiceField(Parametro.objects.filter(estudio=pk_estudio), widget=forms.Select(attrs={'class': 'form-control'}))
    return render(request, 'hc/valor_editar.html', {'form':form, 'estudio':estudio, 'resultado':resultado})

@login_required
def consulta_editar(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.POST:
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.fecha = consulta.fecha
            consulta.save()
            return redirect('hc_editar', pk=consulta.paciente.pk)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'hc/consulta_editar.html', {'form': form, 'consulta':consulta})

@login_required
def consulta_eliminar(request, pk):
    pass
