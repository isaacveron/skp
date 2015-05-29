# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0019_sprint_restante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='Fecha_inicio',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
