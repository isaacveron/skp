# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0015_auto_20150608_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Duracion',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='Restante',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 8, 22, 24, 21, 735019)),
            preserve_default=True,
        ),
    ]
