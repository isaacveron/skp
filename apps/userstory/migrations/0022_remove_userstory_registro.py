# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0021_userstory_registro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='Registro',
        ),
    ]
