# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('summoner_name', models.CharField(unique=True, max_length=50)),
                ('date_of_registration', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date joined')),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
