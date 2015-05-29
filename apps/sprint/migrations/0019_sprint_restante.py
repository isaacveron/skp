# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0018_sprint_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Restante',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
