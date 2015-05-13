# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(unique=True, max_length=30)),
                ('Descripcion', models.TextField()),
                ('Fecha_inicio', models.DateField(verbose_name=b'Fecha de inicio')),
                ('Fecha_finalizacion', models.DateField(verbose_name=b'Fecha de finalizacion')),
                ('Cliente', models.CharField(max_length=30)),
                ('Estado', models.CharField(default=b'Pendiente', max_length=15)),
                ('Grupo_trabajo', models.ManyToManyField(related_name='Proyectos', to=settings.AUTH_USER_MODEL)),
                ('Scrum_Master', models.ForeignKey(related_name='Scrum_Master', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
