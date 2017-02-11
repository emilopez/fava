# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0030_auto_20170211_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='motivo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
