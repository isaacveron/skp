# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0012_auto_20150430_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='Nombre',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
