# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0011_auto_20150509_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sprint',
            options={'permissions': (('iniciar_sprint', 'puede iniciar el sprint'), ('detener_sprint', 'puede detener el sprint'), ('cambiar_estado_sprint', 'puede cambiar el estado del sprint'))},
        ),
    ]
