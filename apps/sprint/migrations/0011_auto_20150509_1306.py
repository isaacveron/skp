# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0010_auto_20150430_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='Duracion',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
