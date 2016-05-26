# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0005_auto_20160514_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(max_length=6, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab',
                                   choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')]),
        ),
    ]
