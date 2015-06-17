# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.userstory.models


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0022_remove_userstory_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Registro',
            field=apps.userstory.models.ListField(null=True),
            preserve_default=True,
        ),
    ]
