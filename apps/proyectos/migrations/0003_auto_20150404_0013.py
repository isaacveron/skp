# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20150404_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Cliente',
            field=models.CharField(max_length=30, null=True),
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
