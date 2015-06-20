# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0038_auto_20150618_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 14, 25, 16, 847945)),
            preserve_default=True,
        ),
    ]
