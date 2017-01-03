# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0023_estudio_parametro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametro',
            name='estudio',
            field=models.ForeignKey(to='hc.Estudio', related_name='parametros'),
        ),
    ]
