# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0044_auto_20170226_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='paciente',
            field=models.ForeignKey(to='hc.Paciente', related_name='historicos'),
        ),
    ]
