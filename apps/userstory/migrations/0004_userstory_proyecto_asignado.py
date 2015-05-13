# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_auto_20150411_1533'),
        ('userstory', '0003_remove_userstory_sprints'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Proyecto_asignado',
            field=models.ForeignKey(to='proyectos.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
