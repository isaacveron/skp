# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0032_auto_20150617_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 9, 11, 11, 980435)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Estado',
            field=models.CharField(default=b'Activo', max_length=30, choices=[(b'Activo', b'Activo'), (b'Terminado', b'Terminado'), (b'Cancelado', b'Cancelado')]),
            preserve_default=True,
        ),
    ]
