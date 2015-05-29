# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.sprint.models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0017_remove_sprint_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Registro',
            field=apps.sprint.models.ListField(null=True),
            preserve_default=True,
        ),
    ]
