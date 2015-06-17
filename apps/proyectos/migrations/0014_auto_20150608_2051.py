# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import apps.proyectos.models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0013_auto_20150529_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Registro',
            field=apps.proyectos.models.ListField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 8, 20, 51, 1, 913802)),
            preserve_default=True,
        ),
    ]
