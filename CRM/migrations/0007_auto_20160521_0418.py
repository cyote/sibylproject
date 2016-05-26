# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CRM', '0006_auto_20160515_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject',
                 models.CharField(max_length=30, verbose_name=b'\xe9\xa2\x84\xe7\xba\xa6\xe4\xb8\xbb\xe9\xa2\x98')),
                ('time_slot', models.CharField(max_length=4, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4\xe6\xae\xb5',
                                               choices=[(b'AM', b'10:00-11:00'), (b'PM', b'15:00-16:00')])),
                ('confirm_status',
                 models.CharField(max_length=2, verbose_name=b'\xe7\xa1\xae\xe8\xae\xa4\xe7\x8a\xb6\xe6\x80\x81',
                                  choices=[(b'un', b'\xe6\x9c\xaa\xe7\xa1\xae\xe8\xae\xa4'),
                                           (b'co', b'\xe5\xb7\xb2\xe5\x88\xb0\xe8\xae\xbf'),
                                           (b'ab', b'\xe7\xbc\xba\xe5\xb8\xad')])),
                ('date', models.DateField(verbose_name=b'\xe9\xa2\x84\xe7\xba\xa6\xe6\x97\xa5\xe6\x9c\x9f')),
                ('comment', models.TextField(max_length=100, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': '\u54a8\u8be2\u9884\u7ea6',
                'verbose_name_plural': '\u54a8\u8be2\u9884\u7ea6',
            },
        ),
        migrations.CreateModel(
            name='Returning_call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4',
                                              auto_created=True)),
                ('comment',
                 models.TextField(max_length=1000, verbose_name=b'\xe5\x9b\x9e\xe8\xae\xbf\xe8\xae\xb0\xe5\xbd\x95')),
                ('call_date', models.DateTimeField(verbose_name=b'\xe5\x9b\x9e\xe8\xae\xbf\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ('-call_date',),
                'verbose_name': '\u56de\u8bbf\u8bb0\u5f55',
                'verbose_name_plural': '\u56de\u8bbf\u8bb0\u5f55',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='client_type',
            field=models.CharField(default=b'student', max_length=8,
                                   verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b', blank=True,
                                   choices=[(b'student', b'\xe5\xad\xa6\xe7\x94\x9f'),
                                            (b'parent', b'\xe5\xae\xb6\xe9\x95\xbf'),
                                            (b'adault', b'\xe6\x88\x90\xe4\xba\xba')]),
        ),
        migrations.AddField(
            model_name='client',
            name='leads_source',
            field=models.CharField(max_length=30,
                                   verbose_name=b'\xe4\xbd\x95\xe5\xa4\x84\xe5\xbe\x97\xe7\x9f\xa5\xe6\x88\x91\xe4\xbb\xac',
                                   blank=True),
        ),
        migrations.AddField(
            model_name='returning_call',
            name='client',
            field=models.ForeignKey(related_name='returning_calls',
                                    verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d', to='CRM.Client'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(related_name='appointments',
                                    verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d', to='CRM.Client'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='record',
            field=models.OneToOneField(related_name='appointments',
                                       verbose_name=b'\xe5\x92\xa8\xe8\xaf\xa2\xe8\xae\xb0\xe5\xbd\x95',
                                       to='CRM.Record'),
        ),
    ]
