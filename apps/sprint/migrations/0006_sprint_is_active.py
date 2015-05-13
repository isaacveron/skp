# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0005_sprint_duracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
