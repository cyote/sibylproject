# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0003_auto_20160512_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='body',
            field=models.TextField(max_length=2000, verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
    ]
