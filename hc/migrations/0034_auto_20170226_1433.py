# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0033_auto_20170226_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='entrada',
            field=tinymce.models.HTMLField(default='><'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='motivo',
            field=tinymce.models.HTMLField(default='><'),
        ),
    ]
