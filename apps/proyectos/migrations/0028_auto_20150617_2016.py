# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0027_auto_20150617_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateField(default=datetime.datetime(2015, 6, 17, 20, 16, 54, 249291)),
            preserve_default=True,
        ),
    ]
