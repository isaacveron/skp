# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0007_sprint_flujo_asignado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprint',
            old_name='Flujo_asignado',
            new_name='Tabla_asignada',
        ),
    ]
