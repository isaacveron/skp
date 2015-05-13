# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_auto_20150411_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
