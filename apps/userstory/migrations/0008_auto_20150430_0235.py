# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0007_auto_20150429_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='actividad_asignada',
        ),
        migrations.RemoveField(
            model_name='userstory',
            name='estado_actividad',
        ),
    ]
