# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0019_userstory_prioridad'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Bloqueado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
