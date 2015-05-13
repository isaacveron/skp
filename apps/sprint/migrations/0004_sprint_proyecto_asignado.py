# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_auto_20150411_1533'),
        ('sprint', '0003_sprint_userstorys'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Proyecto_asignado',
            field=models.ForeignKey(to='proyectos.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
