# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='obra_social',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
