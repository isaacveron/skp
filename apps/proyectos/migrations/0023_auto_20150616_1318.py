# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0022_auto_20150616_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='sprin_activo',
            new_name='sprint_activo',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Dia_actual',
            field=models.DateField(default=datetime.datetime(2015, 6, 16, 13, 18, 45, 831179)),
            preserve_default=True,
        ),
    ]
