# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0023_auto_20150616_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateField(default=datetime.datetime(2015, 6, 16, 13, 20, 28, 729735)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Fecha_finalizacion',
            field=models.DateField(null=True, verbose_name=b'Fecha de finalizacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Fecha_inicio',
            field=models.DateField(null=True, verbose_name=b'Fecha de inicio'),
            preserve_default=True,
        ),
    ]
