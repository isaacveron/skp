# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0014_remove_sprint_restringido'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Registro',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
