# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0026_auto_20170109_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resultado',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='resultado',
            name='estudio',
            field=models.ForeignKey(to='hc.Estudio'),
        ),
    ]
