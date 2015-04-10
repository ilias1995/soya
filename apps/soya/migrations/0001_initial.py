# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soyainfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soya_sort', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('image', models.ImageField(upload_to=b'/soyaimage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
