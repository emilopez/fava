# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0013_auto_20161204_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='antecedentes',
            field=models.ManyToManyField(to='hc.Antecedente', related_name='paciente_antecedente', through='hc.PacienteAntecedente'),
        ),
    ]
