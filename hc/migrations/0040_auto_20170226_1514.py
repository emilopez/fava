# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0039_auto_20170226_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='entrada',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='motivo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
