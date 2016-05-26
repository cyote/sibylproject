# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0008_auto_20160521_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returning_call',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True,
                                       verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
