# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0012_auto_20160522_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='appointment',
            field=models.ForeignKey(related_name='records',
                                    verbose_name=b'\xe9\xa2\x84\xe7\xba\xa6\xe8\xae\xb0\xe5\xbd\x95',
                                    to='CRM.Appointment'),
        ),
    ]
