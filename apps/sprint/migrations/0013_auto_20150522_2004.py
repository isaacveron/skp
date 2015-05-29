# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0012_auto_20150513_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Prioridad_mas_alta',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sprint',
            name='Restringido',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sprint',
            name='UserStorys',
            field=models.ManyToManyField(related_name='sprint', null=True, to='userstory.UserStory'),
            preserve_default=True,
        ),
    ]
