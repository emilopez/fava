# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0025_resultado_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='estudio',
            field=models.ForeignKey(related_name='estudios', to='hc.Estudio'),
        ),
    ]
