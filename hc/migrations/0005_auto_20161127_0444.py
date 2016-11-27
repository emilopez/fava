# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0004_auto_20161125_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='medico',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
