# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc', '0018_auto_20161204_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pacienteantecedente',
            name='antecedente',
        ),
        migrations.RemoveField(
            model_name='pacienteantecedente',
            name='paciente',
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='registros',
            field=models.ManyToManyField(through='hc.Historico', to='hc.Paciente'),
        ),
        migrations.DeleteModel(
            name='PacienteAntecedente',
        ),
        migrations.AddField(
            model_name='historico',
            name='antecedente',
            field=models.ForeignKey(to='hc.Antecedente'),
        ),
        migrations.AddField(
            model_name='historico',
            name='paciente',
            field=models.ForeignKey(to='hc.Paciente'),
        ),
    ]
