# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0024_auto_20170103_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('lugar', models.TextField(blank=True, null=True)),
                ('estudio', models.ForeignKey(to='hc.Estudio')),
                ('paciente', models.ForeignKey(to='hc.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('parametro', models.ForeignKey(to='hc.Parametro')),
                ('resultado', models.ForeignKey(to='hc.Resultado')),
            ],
        ),
    ]
