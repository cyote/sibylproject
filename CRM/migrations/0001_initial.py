# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('gender', models.CharField(max_length=2, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')])),
                ('phone', models.CharField(max_length=13, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f')),
                ('birthday', models.DateField(verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('comments', models.TextField(max_length=100, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('client_status', models.CharField(default=b'leads', max_length=10, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'leads', b'\xe6\xbd\x9c\xe5\x9c\xa8\xe5\xae\xa2\xe6\x88\xb7'), (b'normal', b'\xe6\xad\xa3\xe5\xbc\x8f\xe5\xae\xa2\xe6\x88\xb7'), (b'end', b'\xe5\xb7\xb2\xe7\xbb\x93\xe6\xa1\x88')])),
                ('adress', models.CharField(max_length=50, verbose_name=b'\xe4\xbd\x8f\xe5\x9d\x80')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False, verbose_name=b'\xe5\x9c\xa8\xe6\xa1\x88\xe5\xae\xa2\xe6\x88\xb7')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
