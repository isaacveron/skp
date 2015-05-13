# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0002_auto_20150421_0112'),
        ('userstory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Sprints',
            field=models.ManyToManyField(related_name='Sprints', null=True, to='sprint.Sprint'),
            preserve_default=True,
        ),
    ]
