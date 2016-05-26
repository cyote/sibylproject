# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0014_client_vip_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='vip_class',
            field=models.CharField(default=b'no', max_length=4, verbose_name=b'VIP\xe7\xba\xa7\xe5\x88\xab',
                                   choices=[(b'no', b'\xe6\x97\xa0'), (b'1', b'VIP1'), (b'2', b'VIP2'), (b'3', b'VIP3'),
                                            (b'life', b'\xe7\xbb\x88\xe8\xba\xab\xe5\x88\xb6')]),
        ),
    ]
