# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soya', '0003_zakaz'),
    ]

    operations = [
        migrations.AddField(
            model_name='zakaz',
            name='how_many',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zakaz',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zakaz',
            name='soya_sort',
            field=models.CharField(default=2, max_length=200, choices=[(b'\xd0\x9f', b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x81\xd0\xbe\xd1\x80\xd1\x82'), (b'\xd0\x92', b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xbe\xd1\x80\xd1\x82'), (b'\xd0\xa2', b'\xd0\xa2\xd1\x80\xd0\xb5\xd1\x82\xd0\xb8\xd0\xb9 \xd1\x81\xd0\xbe\xd1\x80\xd1\x82')]),
            preserve_default=False,
        ),
    ]
