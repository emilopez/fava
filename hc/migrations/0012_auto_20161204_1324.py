# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0011_auto_20161202_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('texto', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HcAntDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('antecedente', models.ForeignKey(to='hc.Antecedente')),
            ],
        ),
        migrations.CreateModel(
            name='TipoAntecedente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('texto', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='antecedentes_heredofamiliares',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='antecedentes_personales',
        ),
        migrations.AddField(
            model_name='hcantdetalle',
            name='historia_clinica',
            field=models.ForeignKey(to='hc.HistoriaClinica'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='tipo',
            field=models.ForeignKey(related_name='antecedentes', to='hc.TipoAntecedente'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='antecedentes',
            field=models.ManyToManyField(through='hc.HcAntDetalle', to='hc.Antecedente'),
        ),
    ]
