# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0010_auto_20161202_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='historia_clinica',
            field=models.ForeignKey(related_name='consultas', to='hc.HistoriaClinica'),
        ),
    ]
