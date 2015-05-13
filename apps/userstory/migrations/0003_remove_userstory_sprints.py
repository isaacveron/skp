# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0002_userstory_sprints'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='Sprints',
        ),
    ]
