# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='estado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
