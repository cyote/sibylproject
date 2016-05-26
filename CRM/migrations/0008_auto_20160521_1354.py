# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0007_auto_20160521_0418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='returning_call',
            old_name='date',
            new_name='created_date',
        ),
    ]
