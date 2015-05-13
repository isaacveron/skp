# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0005_auto_20150422_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='flujo',
            name='Copia',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
