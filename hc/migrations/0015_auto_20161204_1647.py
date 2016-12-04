# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0014_auto_20161204_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='antecedentes',
            new_name='registros_antecedentes',
        ),
    ]
