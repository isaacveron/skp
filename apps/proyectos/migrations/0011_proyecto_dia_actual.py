# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0010_auto_20150501_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 21, 55, 31, 487073)),
            preserve_default=True,
        ),
    ]
