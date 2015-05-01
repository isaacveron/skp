# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0008_auto_20150430_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='in_kanban',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userstory',
            name='Estado',
            field=models.CharField(default=b'Pendiente', max_length=15, choices=[(b'AsignadoSprint', b'AsignadoSprint'), (b'AsignadoFlujo', b'AsignadoFlujo'), (b'AsignadoSprintActivo', b'AsignadoSprintActivo'), (b'Resuelta', b'Resuelta'), (b'Cancelado', b'Cancelado'), (b'Terminado', b'Terminado')]),
            preserve_default=True,
        ),
    ]
