# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0014_cargarhoras'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Sub_version',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstory',
            name='Version',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
