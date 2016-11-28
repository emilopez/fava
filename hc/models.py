from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    NACIONALIDAD_CHOICES=(
        ('Argentina', 'Argentino'),
        ('Boliviana', 'Boliviano'),
        ('Brasilera', 'Brasilero'),
        ('Colombiana', 'Colombiano'),
        ('Chilena', 'Chileno'),
        ('Paraguaya', 'Paraguayo'),
        ('Peruana', 'Peruano'),
        ('Uruguaya', 'Uruguayo'),
        ('Otra','Otro'), )
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    documento = models.CharField(max_length=15, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length= 25, choices=NACIONALIDAD_CHOICES, default=('Argentina', 'Argentino'))
    estado_civil = models.CharField(max_length=30, choices=(('C', 'Casado/a'), ('S', 'Soltero/a')))
    sexo = models.CharField(max_length=30, choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
    ocupacion = models.CharField(max_length = 50, null=True, blank=True)
    domicilio = models.CharField(max_length = 100, null=True, blank=True)
    telefono = models.CharField(max_length = 50, null=True, blank=True)
    obra_social = models.CharField(max_length = 30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

class Consulta(models.Model):
    paciente = models.ForeignKey('hc.Paciente', related_name='consultas')
    fecha = models.DateTimeField(auto_now=True)   # Almacena la fecha actual
    entrada = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-fecha"]

class Adjunto(models.Model):
    consulta = models.ForeignKey("hc.Consulta")
    archivo = models.FileField(blank=True, null=True, upload_to="Consulta")
