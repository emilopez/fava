# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0002_auto_20161125_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
