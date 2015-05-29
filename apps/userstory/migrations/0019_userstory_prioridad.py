# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0018_auto_20150513_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Prioridad',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
