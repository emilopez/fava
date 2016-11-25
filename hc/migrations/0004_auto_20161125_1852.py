# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0003_profesional_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
