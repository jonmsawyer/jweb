# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
