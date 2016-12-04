# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0009_auto_20161202_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('antecedentes_personales', models.TextField(null=True, blank=True)),
                ('antecedentes_heredofamiliares', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='antecedentes_heredofamiliares',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='antecedentes_personales',
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='paciente',
            field=models.ForeignKey(to='hc.Paciente', related_name='historia_clinica'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='historia_clinica',
            field=models.ForeignKey(null=True, blank=True, related_name='consultas', to='hc.HistoriaClinica'),
        ),
    ]
