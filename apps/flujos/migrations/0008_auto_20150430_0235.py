# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0008_auto_20150430_0235'),
        ('flujos', '0007_auto_20150430_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='to_do',
        ),
        migrations.AddField(
            model_name='actividad',
            name='Doing',
            field=models.ManyToManyField(related_name='doing', null=True, to='userstory.UserStory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='Done',
            field=models.ManyToManyField(related_name='Done', null=True, to='userstory.UserStory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='To_do',
            field=models.ManyToManyField(related_name='To_do', null=True, to='userstory.UserStory'),
            preserve_default=True,
        ),
    ]
