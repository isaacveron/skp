# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0004_auto_20150422_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='idTabla',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flujo',
            name='Actividades',
            field=models.ManyToManyField(to='flujos.Actividad', null=True),
            preserve_default=True,
        ),
    ]
