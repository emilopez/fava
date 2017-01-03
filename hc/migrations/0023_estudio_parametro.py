# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0022_auto_20161208_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField()),
                ('estudio', models.ForeignKey(to='hc.Estudio')),
            ],
        ),
    ]
