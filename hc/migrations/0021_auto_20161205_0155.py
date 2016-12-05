# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0020_auto_20161205_0149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historico',
            options={'ordering': ['antecedente']},
        ),
    ]
