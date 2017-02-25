# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0031_consulta_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='entrada',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='motivo',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
    ]
