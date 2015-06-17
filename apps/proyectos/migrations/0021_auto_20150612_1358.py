# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0020_auto_20150612_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateField(default=datetime.datetime(2015, 6, 12, 13, 58, 44, 453089)),
            preserve_default=True,
        ),
    ]
