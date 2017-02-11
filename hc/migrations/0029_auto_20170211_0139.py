# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0028_auto_20170113_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
