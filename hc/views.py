from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Profesional, Antecedente, TipoAntecedente, Estudio, Parametro, Resultado, Consulta, Historico, Valor
from .forms import PacienteForm, ConsultaForm, AntecedenteForm, TipoAntecedenteForm, EstudioForm, ParametroForm, HistoricoForm, ResultadoForm, ValorForm
from django.forms.formsets import formset_factory
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
            return redirect('hc_consultas', pk=paciente.pk)
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
            return redirect('hc_consultas', pk=paciente.pk)
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
def hc_consulta_editar(request, pk, pk_consulta):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    consulta = get_object_or_404(Consulta, pk=pk_consulta)
    if request.POST:
        form_consulta = ConsultaForm(request.POST, instance=consulta)
        if form_consulta.is_valid():
            consulta = form_consulta.save(commit=False)
            consulta.save()
            return redirect('hc_consultas', pk=pk)
    else:
        print("NO fue un post")
        form_consulta = ConsultaForm(instance=consulta)
    return render(request, 'hc/hc_consultas.html', {'paciente': paciente, 'form_consulta':form_consulta, 'consulta':consulta})

@login_required
def hc_consulta_eliminar(request, pk, pk_consulta):
    consulta = get_object_or_404(Consulta, pk=pk_consulta)
    consulta.delete()
    return redirect('hc_consultas', pk=pk)

# @login_required
# def hc_antecedentes(request, pk):
#     paciente = get_object_or_404(Paciente, pk=pk)
#     paciente.set_edad()
#     if request.POST:
#         form_historico_antecedente = HistoricoForm(request.POST)
#         if form_historico_antecedente.is_valid():
#             historico_antecedente = form_historico_antecedente.save(commit=False)
#             historico_antecedente.paciente = paciente
#             historico_antecedente.save()
#         return redirect('hc_antecedentes', pk=pk)
#     else:
#         form_historico_antecedente = HistoricoForm()
#     return render(request, 'hc/hc_antecedentes.html', {'paciente': paciente, 'form_historico_antecedente':form_historico_antecedente})

@login_required
def hc_antecedente_editar(request, pk, pk_antecedente):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    historico = get_object_or_404(Historico, pk=pk_antecedente)
    if request.POST:
        form_historico_antecedente = HistoricoForm(request.POST, instance=historico)
        if form_historico_antecedente.is_valid():
            historico_antecedente = form_historico_antecedente.save(commit=False)
            # historico_antecedente.paciente = paciente
            historico_antecedente.save()
        return redirect('hc_antecedentes', pk=pk)
    else:
        form_historico_antecedente = HistoricoForm(instance=historico)
    return render(request, 'hc/hc_antecedentes.html', {'paciente': paciente, 'form_historico_antecedente':form_historico_antecedente, 'historico':historico})

@login_required
def hc_antecedente_eliminar(request, pk, pk_antecedente):
    historico = get_object_or_404(Historico, pk=pk_antecedente)
    historico.delete()
    return redirect('hc_antecedentes', pk=historico.paciente.pk)

@login_required
def hc_antecedentes(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.set_edad()
    antecedentes = Antecedente.objects.all()
    HistoricoFormSet = formset_factory(HistoricoForm, extra=len(antecedentes))
    if request.POST:
        formset = HistoricoFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get('texto', False):
                    historico = form.save(commit=False)
                    historico.paciente = paciente
                    historico.save()
        return redirect('hc_antecedentes', pk=pk)
    else:

        formset = HistoricoFormSet()
        i = 0
        for f in formset:
            f.fields['antecedente'] = forms.ModelChoiceField(antecedentes, widget=forms.Select(attrs={'class': 'form-control'}))
            f.fields['antecedente'].initial = antecedentes[i]
            f.fields['texto'].label = str(antecedentes[i]).capitalize()
            f.fields['texto'].label_suffix = ""
            f.fields['tipo'] = forms.CharField(label=str(antecedentes[i].tipo).capitalize(), label_suffix="")

            i += 1
        return render(request, 'hc/hc_antecedentes2.html', {'paciente': paciente, 'formset':formset})

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
def valor_nuevo(request, pk_resultado):
    resultado = get_object_or_404(Resultado, pk=pk_resultado)
    pk_estudio = resultado.estudio.pk
    estudio = get_object_or_404(Estudio, pk=pk_estudio)
    parametros = Parametro.objects.filter(estudio=pk_estudio)
    ValorFormSet = formset_factory(ValorForm, extra=len(parametros))
    if request.POST:
        formset = ValorFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data['texto']:
                    valor = form.save(commit=False)
                    valor.resultado = resultado
                    valor.save()
        return redirect('valor_nuevo', pk_resultado=pk_resultado)
    else:
        formset = ValorFormSet()
        i = 0
        for f in formset:
            f.fields['parametro'] = forms.ModelChoiceField(parametros, widget=forms.Select(attrs={'class': 'form-control'}))
            f.fields['parametro'].initial = parametros[i]
            f.fields['texto'].label = str(parametros[i])
            i += 1
            # f.fields['parametro'].choices = [(i.id, str(i).upper()) for i in parametros]
        return render(request, 'hc/valor_editar.html', {'formset':formset, 'estudio':estudio, 'resultado':resultado})

def valor_eliminar(request, pk):
    valor = get_object_or_404(Valor, pk=pk)
    valor.delete()
    return redirect('valor_nuevo', pk_resultado=valor.resultado.pk)

def resultado_eliminar(request, pk):
    resultado = get_object_or_404(Resultado, pk=pk)
    resultado.delete()
    return redirect('hc_estudios', pk=resultado.paciente.pk)
