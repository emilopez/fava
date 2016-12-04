# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0012_auto_20161204_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteAntecedente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('texto', models.TextField(null=True, blank=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('antecedente', models.ForeignKey(to='hc.Antecedente')),
                ('paciente', models.ForeignKey(to='hc.Paciente')),
            ],
        ),
        migrations.RemoveField(
            model_name='hcantdetalle',
            name='antecedente',
        ),
        migrations.RemoveField(
            model_name='hcantdetalle',
            name='historia_clinica',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='antecedentes',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='historia_clinica',
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(related_name='consultas', null=True, blank=True, to='hc.Paciente'),
        ),
        migrations.DeleteModel(
            name='HcAntDetalle',
        ),
        migrations.DeleteModel(
            name='HistoriaClinica',
        ),
        migrations.AddField(
            model_name='paciente',
            name='antecedentes',
            field=models.ManyToManyField(to='hc.Antecedente', through='hc.PacienteAntecedente'),
        ),
    ]
