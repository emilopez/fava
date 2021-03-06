from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.pacientes, name='pacientes'),
    url(r'^paciente/(?P<pk>\d+)/$', views.paciente_detalle, name='paciente_detalle'),
    url(r'^paciente/nuevo/$', views.paciente_nuevo, name='paciente_nuevo'),
    url(r'^paciente/(?P<pk>\d+)/editar/$', views.paciente_editar, name='paciente_editar'),
    url(r'^paciente/(?P<pk>\d+)/eliminar/$', views.paciente_eliminar, name='paciente_eliminar'),
    url(r'^paciente/(?P<pk>\d+)/consultas$', views.hc_consultas, name='hc_consultas'),
    url(r'^paciente/(?P<pk>\d+)/consulta/(?P<pk_consulta>\d+)$', views.hc_consulta_editar, name='hc_consulta_editar'),
    url(r'^paciente/(?P<pk>\d+)/consulta/(?P<pk_consulta>\d+)/eliminar$', views.hc_consulta_eliminar, name='hc_consulta_eliminar'),
    #url(r'^paciente/(?P<pk>\d+)/antecedentes$', views.hc_antecedentes, name='hc_antecedentes'),
    url(r'^paciente/(?P<pk>\d+)/antecedentes$', views.hc_antecedentes, name='hc_antecedentes'),
    url(r'^paciente/(?P<pk>\d+)/antecedente/(?P<pk_antecedente>\d+)$', views.hc_antecedente_editar, name='hc_antecedente_editar'),
    url(r'^paciente/(?P<pk>\d+)/antecedente/(?P<pk_antecedente>\d+)/eliminar/$', views.hc_antecedente_eliminar, name='hc_antecedente_eliminar'),
    url(r'^paciente/(?P<pk>\d+)/estudios$', views.hc_estudios, name='hc_estudios'),
    url(r'^resultado/(?P<pk_resultado>\d+)/nuevovalor$', views.valor_nuevo, name='valor_nuevo'),
    url(r'^resultado/(?P<pk>\d+)/eliminar$', views.resultado_eliminar, name='resultado_eliminar'),
    url(r'^valor/(?P<pk>\d+)/eliminar$', views.valor_eliminar, name='valor_eliminar'),
    url(r'^antecedente/nuevo/$', views.antecedente_nuevo, name='antecedente_nuevo'),
    url(r'^antecedente/listar/$', views.antecedentes, name='antecedentes'),
    url(r'^tipoantecedente/listar/$', views.tipo_antecedente_listar, name='tipo_antecedente_listar'),
    url(r'^estudio/nuevo/$', views.estudio_nuevo, name='estudio_nuevo'),
    url(r'^estudio/(?P<pk>\d+)/eliminar/$', views.estudio_eliminar, name='estudio_eliminar'),
    url(r'^parametro/(?P<pk>\d+)/eliminar/$', views.parametro_eliminar, name='parametro_eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
