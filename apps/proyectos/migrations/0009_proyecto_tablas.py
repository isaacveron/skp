# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0005_auto_20150422_1934'),
        ('proyectos', '0008_remove_proyecto_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Tablas',
            field=models.ManyToManyField(to='flujos.Flujo', null=True),
            preserve_default=True,
        ),
    ]
