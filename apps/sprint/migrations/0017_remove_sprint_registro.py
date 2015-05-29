# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0016_auto_20150528_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='Registro',
        ),
    ]
