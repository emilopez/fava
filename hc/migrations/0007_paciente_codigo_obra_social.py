# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0006_auto_20161130_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='codigo_obra_social',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
    ]
