# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0009_auto_20150430_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='Estado',
            field=models.CharField(default=b'Pendiente', max_length=30, choices=[(b'AsignadoSprint', b'AsignadoSprint'), (b'AsignadoFlujo', b'AsignadoFlujo'), (b'AsignadoSprintActivo', b'AsignadoSprintActivo'), (b'Resuelta', b'Resuelta'), (b'Cancelado', b'Cancelado'), (b'Terminado', b'Terminado')]),
            preserve_default=True,
        ),
    ]
