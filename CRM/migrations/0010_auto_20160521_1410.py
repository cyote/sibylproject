# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0009_auto_20160521_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='confirm_status',
            field=models.CharField(default=b'un', max_length=2,
                                   verbose_name=b'\xe7\xa1\xae\xe8\xae\xa4\xe7\x8a\xb6\xe6\x80\x81',
                                   choices=[(b'un', b'\xe6\x9c\xaa\xe7\xa1\xae\xe8\xae\xa4'),
                                            (b'co', b'\xe5\xb7\xb2\xe5\x88\xb0\xe8\xae\xbf'),
                                            (b'ab', b'\xe7\xbc\xba\xe5\xb8\xad')]),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='record',
            field=models.OneToOneField(related_name='appointments',
                                       verbose_name=b'\xe5\x92\xa8\xe8\xaf\xa2\xe8\xae\xb0\xe5\xbd\x95', blank=True,
                                       to='CRM.Record'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_slot',
            field=models.CharField(default=b'PM', max_length=4, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4\xe6\xae\xb5',
                                   choices=[(b'AM', b'10:00-11:00'), (b'PM', b'15:00-16:00')]),
        ),
    ]
