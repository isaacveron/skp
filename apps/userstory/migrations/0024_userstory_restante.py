# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0023_userstory_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Restante',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
