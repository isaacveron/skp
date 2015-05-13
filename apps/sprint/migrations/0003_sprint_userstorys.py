# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0003_remove_userstory_sprints'),
        ('sprint', '0002_auto_20150421_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='UserStorys',
            field=models.ManyToManyField(related_name='UserStorys', null=True, to='userstory.UserStory'),
            preserve_default=True,
        ),
    ]
