# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0002_document_estado'),
        ('userstory', '0025_auto_20150608_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargarhoras',
            name='Archivos_adjuntos',
            field=models.ManyToManyField(related_name='archivos_adjuntos', null=True, to='archivos.Document'),
            preserve_default=True,
        ),
    ]
