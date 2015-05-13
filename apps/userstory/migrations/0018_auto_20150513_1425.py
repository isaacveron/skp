# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0017_userstory_duracion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userstory',
            options={'ordering': ['Nombre'], 'permissions': (('avanzar_us', 'puede avanzar el userstory'), ('retroceder_us', 'puede retroceder el userstory'), ('asignar_horas_us', 'puede asignar horas al userstory'), ('cambiar_estado_us', 'cambiar estado del userstory'), ('finalizar_us', 'puede finalizar un userstory'))},
        ),
    ]
