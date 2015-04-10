# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soya', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soya_sort', models.CharField(max_length=200)),
                ('sena', models.IntegerField()),
                ('image', models.ImageField(upload_to=b'soyaimage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='soyainfo',
            name='image',
            field=models.ImageField(upload_to=b'soyaimage'),
            preserve_default=True,
        ),
    ]
