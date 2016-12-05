# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0019_auto_20161204_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antecedente',
            options={'ordering': ['tipo']},
        ),
    ]
