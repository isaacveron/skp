# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='Grupo_trabajo',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='Scrum_Master',
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
