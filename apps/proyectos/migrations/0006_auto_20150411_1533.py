# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_auto_20150404_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Grupo_trabajo',
            field=models.ManyToManyField(related_name='Proyectos', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Scrum_Master',
            field=models.ForeignKey(related_name='Scrum_Master', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
