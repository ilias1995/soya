# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soya', '0004_auto_20150409_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='soya_sort',
            field=models.CharField(max_length=200, choices=[(b'P', b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x81\xd0\xbe\xd1\x80\xd1\x82'), (b'V', b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xbe\xd1\x80\xd1\x82'), (b'T', b'\xd0\xa2\xd1\x80\xd0\xb5\xd1\x82\xd0\xb8\xd0\xb9 \xd1\x81\xd0\xbe\xd1\x80\xd1\x82')]),
            preserve_default=True,
        ),
    ]
