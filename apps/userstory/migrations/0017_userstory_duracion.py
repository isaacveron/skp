# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0016_auto_20150502_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Duracion',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
