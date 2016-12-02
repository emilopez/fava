# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0007_paciente_codigo_obra_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='antecedentes_heredofamiliares',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='antecedentes_personales',
            field=models.TextField(null=True, blank=True),
        ),
    ]
