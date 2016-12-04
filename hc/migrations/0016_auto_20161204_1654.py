# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0015_auto_20161204_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='registros_antecedentes',
        ),
        migrations.AddField(
            model_name='antecedente',
            name='registros_pacientes',
            field=models.ManyToManyField(to='hc.Paciente', related_name='antecedente_paciente', through='hc.PacienteAntecedente'),
        ),
    ]
