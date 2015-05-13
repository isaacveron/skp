# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_auto_20150404_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Usuario_creador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
