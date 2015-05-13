# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0005_userstory_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='Estado',
            field=models.CharField(default=b'Pendiente', max_length=15, choices=[(b'AsignadoSprint', b'AsignadoSprint'), (b'AsignadoFlujo', b'AsignadoFlujo'), (b'Resuelta', b'Resuelta'), (b'Cancelado', b'Cancelado')]),
            preserve_default=True,
        ),
    ]
