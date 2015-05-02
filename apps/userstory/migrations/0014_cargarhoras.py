# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0013_auto_20150501_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargarHoras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Horas', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('Descripcion', models.TextField(null=True)),
                ('US_asignado', models.ForeignKey(to='userstory.UserStory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
