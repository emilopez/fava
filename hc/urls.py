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
    url(r'^paciente/(?P<pk>\d+)/hc/$', views.hc_editar, name='hc_editar'),
    url(r'^resultado/(?P<pk_resultado>\d+)/estudio/(?P<pk_estudio>\d+)/nuevovalor$', views.nuevo_valor, name='nuevo_valor'),
    url(r'^antecedente/nuevo/$', views.antecedente_nuevo, name='antecedente_nuevo'),
    url(r'^antecedente/listar/$', views.antecedentes, name='antecedentes'),
    url(r'^tipoantecedente/listar/$', views.tipo_antecedente_listar, name='tipo_antecedente_listar'),
    url(r'^estudio/nuevo/$', views.estudio_nuevo, name='estudio_nuevo'),
    url(r'^estudio/(?P<pk>\d+)/eliminar/$', views.estudio_eliminar, name='estudio_eliminar'),
    url(r'^parametro/(?P<pk>\d+)/eliminar/$', views.parametro_eliminar, name='parametro_eliminar'),
    url(r'^consulta/(?P<pk>\d+)/editar/$', views.consulta_editar, name='consulta_editar'),
    url(r'^consulta/(?P<pk>\d+)/eliminar/$', views.consulta_eliminar, name='consulta_eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
