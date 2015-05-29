# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0015_sprint_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='Registro',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
