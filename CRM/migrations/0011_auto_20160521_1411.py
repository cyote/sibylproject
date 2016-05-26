# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0010_auto_20160521_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='record',
            field=models.OneToOneField(related_name='appointments', null=True,
                                       verbose_name=b'\xe5\x92\xa8\xe8\xaf\xa2\xe8\xae\xb0\xe5\xbd\x95',
                                       to='CRM.Record'),
        ),
    ]
