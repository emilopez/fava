# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0008_auto_20161202_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estado_civil',
            field=models.CharField(blank=True, null=True, max_length=30, choices=[('C', 'Casado/a'), ('S', 'Soltero/a')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, null=True, max_length=30, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')]),
        ),
    ]
