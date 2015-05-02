# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0013_auto_20150501_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='Estado',
            field=models.CharField(default=b'Pendiente', max_length=30, choices=[(b'Pendiente', b'Pendiente'), (b'AsignadoSprint', b'AsignadoSprint'), (b'AsignadoFlujo', b'AsignadoFlujo'), (b'AsignadoSprintActivo', b'AsignadoSprintActivo'), (b'Resuelta', b'Resuelta'), (b'Cancelado', b'Cancelado'), (b'Terminado', b'Terminado')]),
            preserve_default=True,
        ),
    ]
