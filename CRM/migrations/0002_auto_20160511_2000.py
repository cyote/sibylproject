# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('-created',), 'verbose_name': '\u5ba2\u6237', 'verbose_name_plural': '\u5ba2\u6237'},
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(max_length=5, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')]),
        ),
    ]
