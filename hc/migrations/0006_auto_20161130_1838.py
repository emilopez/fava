# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0005_auto_20161127_0444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consulta',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='adjunto',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='consultas/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='adjunto',
            name='consulta',
            field=models.ForeignKey(related_name='adjuntos', to='hc.Consulta'),
        ),
    ]
