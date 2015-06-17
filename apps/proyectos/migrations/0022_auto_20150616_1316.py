# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0021_auto_20150612_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='sprin_activo',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateField(default=datetime.datetime(2015, 6, 16, 13, 16, 13, 265187)),
            preserve_default=True,
        ),
    ]
