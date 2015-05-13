# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0010_auto_20150430_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='Estado_de_eactividad',
            field=models.CharField(default=b'none', max_length=30, choices=[(b'none', b'none'), (b'to_do', b'to_do'), (b'doing', b'doing'), (b'done', b'done')]),
            preserve_default=True,
        ),
    ]
