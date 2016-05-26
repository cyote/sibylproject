# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0013_auto_20160522_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='vip_class',
            field=models.CharField(default=b'no', max_length=4, verbose_name=b'VIP\xe7\xba\xa7\xe5\x88\xab'),
        ),
    ]
