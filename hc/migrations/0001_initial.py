# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjunto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('archivo', models.FileField(null=True, blank=True, upload_to='Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('entrada', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('apellido', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('documento', models.CharField(max_length=15, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=25, default=('Argentina', 'Argentino'), choices=[('Argentina', 'Argentino'), ('Boliviana', 'Boliviano'), ('Brasilera', 'Brasilero'), ('Colombiana', 'Colombiano'), ('Chilena', 'Chileno'), ('Paraguaya', 'Paraguayo'), ('Peruana', 'Peruano'), ('Uruguaya', 'Uruguayo'), ('Otra', 'Otro')])),
                ('estado_civil', models.CharField(max_length=30, choices=[('C', 'Casado/a'), ('S', 'Soltero/a')])),
                ('sexo', models.CharField(max_length=30, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])),
                ('ocupacion', models.CharField(max_length=50, null=True, blank=True)),
                ('domicilio', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('apellido', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('matricula', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=30)),
                ('user', models.OneToOneField(related_name='profesional', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='medico',
            field=models.ForeignKey(related_name='medico', to='hc.Profesional'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(related_name='consultas', to='hc.Paciente'),
        ),
        migrations.AddField(
            model_name='adjunto',
            name='consulta',
            field=models.ForeignKey(to='hc.Consulta'),
        ),
    ]
