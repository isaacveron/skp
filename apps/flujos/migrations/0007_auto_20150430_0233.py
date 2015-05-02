# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0007_auto_20150429_2108'),
        ('flujos', '0006_flujo_copia'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='to_do',
            field=models.ManyToManyField(to='userstory.UserStory', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flujo',
            name='Nombre',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
