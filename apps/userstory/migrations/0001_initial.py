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
            name='UserStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(unique=True, max_length=30)),
                ('Descripcion', models.TextField(null=True)),
                ('Valor_tecnico', models.PositiveIntegerField(null=True, blank=True)),
                ('Valor_de_negocio', models.PositiveIntegerField(null=True, blank=True)),
                ('Size', models.PositiveIntegerField(null=True, blank=True)),
                ('Estado', models.CharField(default=b'Pendiente', max_length=15)),
                ('Fecha_creacion', models.DateTimeField(auto_now=True, null=True)),
                ('Usuario_asignado', models.ForeignKey(related_name='Usuario_asignado', to=settings.AUTH_USER_MODEL, null=True)),
                ('Usuario_creador', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
