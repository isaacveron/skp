# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0008_auto_20150430_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='Doing',
            field=models.ManyToManyField(related_name='Doing', null=True, to='userstory.UserStory'),
            preserve_default=True,
        ),
    ]
