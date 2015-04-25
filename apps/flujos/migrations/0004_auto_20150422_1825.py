# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0003_auto_20150421_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='Nombre',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
