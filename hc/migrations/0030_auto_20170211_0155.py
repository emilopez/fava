# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0029_auto_20170211_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='fecha',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
