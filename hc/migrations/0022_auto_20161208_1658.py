# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0021_auto_20161205_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='nacionalidad',
        ),
        migrations.AddField(
            model_name='paciente',
            name='lugar_nacimiento',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
