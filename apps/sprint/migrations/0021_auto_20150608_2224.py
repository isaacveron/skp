# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0020_auto_20150528_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='Fecha_inicio',
            field=models.DateField(null=True, verbose_name=b'Fecha de inicio', blank=True),
            preserve_default=True,
        ),
    ]
