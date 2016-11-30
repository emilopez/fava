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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
