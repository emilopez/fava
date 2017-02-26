# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0042_auto_20170226_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='entrada',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='motivo',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
    ]
