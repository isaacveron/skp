# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0003_auto_20150404_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Fecha_creacion',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='Usuario_creador',
            field=models.ForeignKey(related_name='creador', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Cliente',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Fecha_finalizacion',
            field=models.DateField(null=True, verbose_name=b'Fecha de finalizacion', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Fecha_inicio',
            field=models.DateField(null=True, verbose_name=b'Fecha de inicio', blank=True),
            preserve_default=True,
        ),
    ]
