# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0008_auto_20150430_0235'),
        ('sprint', '0006_sprint_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Flujo_asignado',
            field=models.ForeignKey(to='flujos.Flujo', null=True),
            preserve_default=True,
        ),
    ]
