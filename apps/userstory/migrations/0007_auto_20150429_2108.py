# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0005_auto_20150422_1934'),
        ('userstory', '0006_auto_20150429_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='actividad_asignada',
            field=models.ForeignKey(to='flujos.Actividad', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstory',
            name='estado_actividad',
            field=models.CharField(default=b'none', max_length=15, choices=[(b'none', b'none'), (b'to_do', b'to_do'), (b'doing', b'doing'), (b'done', b'done')]),
            preserve_default=True,
        ),
    ]
