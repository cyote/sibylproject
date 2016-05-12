# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0002_auto_20160511_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.CharField(max_length=2000, verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('visit', models.IntegerField(default=0, verbose_name=b'\xe5\x88\xb0\xe8\xae\xbf\xe6\xac\xa1\xe6\x95\xb0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': '\u6765\u8bbf\u7eaa\u5f55',
                'verbose_name_plural': '\u6765\u8bbf\u7eaa\u5f55',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='code',
            field=models.CharField(default=0, max_length=10, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='client',
            name='comments',
            field=models.TextField(max_length=400, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AddField(
            model_name='record',
            name='client',
            field=models.ForeignKey(related_name='records', verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7', to='CRM.Client'),
        ),
    ]
