# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0020_userstory_bloqueado'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Registro',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
