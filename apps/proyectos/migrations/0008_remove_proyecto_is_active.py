# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_proyecto_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='is_active',
        ),
    ]
