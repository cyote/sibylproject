# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0004_auto_20160512_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='school',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xb0\xb1\xe8\xaf\xbb\xe5\xad\xa6\xe6\xa0\xa1',
                                   blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(default=0, unique=True, max_length=10,
                                   verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
    ]
