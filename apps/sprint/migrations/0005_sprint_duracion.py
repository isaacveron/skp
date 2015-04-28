# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0004_sprint_proyecto_asignado'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Duracion',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
