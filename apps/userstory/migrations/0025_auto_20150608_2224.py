# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0024_userstory_restante'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Fecha_finalizacion',
            field=models.DateField(null=True, verbose_name=b'Fecha de finalizacion', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstory',
            name='Fecha_inicio',
            field=models.DateField(null=True, verbose_name=b'Fecha de inicio', blank=True),
            preserve_default=True,
        ),
    ]
