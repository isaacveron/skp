# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0009_auto_20150430_2241'),
        ('userstory', '0011_userstory_estado_de_eactividad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstory',
            old_name='Estado_de_eactividad',
            new_name='Estado_de_actividad',
        ),
        migrations.AddField(
            model_name='userstory',
            name='Actividad_asignada',
            field=models.ForeignKey(to='flujos.Actividad', null=True),
            preserve_default=True,
        ),
    ]
