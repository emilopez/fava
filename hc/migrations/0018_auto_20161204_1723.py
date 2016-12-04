# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0017_auto_20161204_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antecedente',
            old_name='registros_pacientes',
            new_name='registros',
        ),
    ]
