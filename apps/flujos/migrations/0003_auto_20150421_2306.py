# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0002_auto_20150410_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='Orden',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flujo',
            name='Actividades',
            field=models.ManyToManyField(to='flujos.Actividad', blank=True),
            preserve_default=True,
        ),
    ]
