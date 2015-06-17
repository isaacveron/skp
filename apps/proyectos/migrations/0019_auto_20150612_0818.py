# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0018_auto_20150609_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 8, 18, 5, 16363)),
            preserve_default=True,
        ),
    ]
