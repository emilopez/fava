from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os

class Profesional(models.Model):
    user = models.OneToOneField(User, related_name='profesional')
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    matricula = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "{} {} (MP {})".format(self.nombre, self.apellido, self.matricula)

class Paciente(models.Model):
    medico = models.ForeignKey('auth.User')
    NACIONALIDAD_CHOICES=(('Argentina', 'Argentino'), ('Boliviana', 'Boliviano'),  ('Brasilera', 'Brasilero'), ('Colombiana', 'Colombiano'),
        ('Chilena', 'Chileno'), ('Paraguaya', 'Paraguayo'), ('Peruana', 'Peruano'), ('Uruguaya', 'Uruguayo'), ('Otra','Otro'),)
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    obra_social = models.CharField(max_length = 30, null=True, blank=True)
    codigo_obra_social = models.CharField(max_length = 30, null=True, blank=True)
    documento = models.CharField(max_length=15, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length= 25, choices=NACIONALIDAD_CHOICES, default=('Argentina', 'Argentino'))
    estado_civil = models.CharField(max_length=30, null=True, blank=True, choices=(('C', 'Casado/a'), ('S', 'Soltero/a')))
    sexo = models.CharField(max_length=30, null=True, blank=True, choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
    ocupacion = models.CharField(max_length = 50, null=True, blank=True)
    domicilio = models.CharField(max_length = 100, null=True, blank=True)
    telefono = models.CharField(max_length = 50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Consulta(models.Model):
    paciente = models.ForeignKey('hc.Paciente', related_name='consultas',null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)   # Almacena la fecha actual
    entrada = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return "{} {}".format(self.paciente, self.fecha)

class Adjunto(models.Model):
    consulta = models.ForeignKey("hc.Consulta", related_name='adjuntos')
    archivo = models.FileField(blank=True, null=True, upload_to="consultas/%Y/%m/%d/")
    def filename(self):
        return os.path.basename(self.archivo.name)

class TipoAntecedente(models.Model):
    texto = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.texto)

class Antecedente(models.Model):
    tipo = models.ForeignKey("hc.TipoAntecedente", related_name='antecedentes')
    texto = models.TextField(blank=True, null=True)
    registros = models.ManyToManyField('hc.Paciente', through = 'hc.Historico')

    class Meta:
        ordering = ["tipo"]

    def __str__(self):
        return "{}-{}".format(self.tipo, self.texto)

class Historico(models.Model):
    """ tabla intermedia totalmente dependiente de paciente-antecedente"""
    paciente = models.ForeignKey('hc.Paciente')
    antecedente = models.ForeignKey('hc.Antecedente')
    texto = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["antecedente"]
    def __str__(self):
        return "{}-{}".format(self.paciente, self.antecedente)
