# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0016_auto_20161204_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedente',
            name='registros_pacientes',
            field=models.ManyToManyField(to='hc.Paciente', through='hc.PacienteAntecedente'),
        ),
    ]
