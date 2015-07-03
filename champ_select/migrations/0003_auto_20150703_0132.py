# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('champ_select', '0002_auto_20150703_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='champion',
        ),
        migrations.AddField(
            model_name='champion',
            name='date_created',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
        ),
        migrations.AddField(
            model_name='champion',
            name='games',
            field=models.ManyToManyField(to='champ_select.Game'),
        ),
        migrations.AddField(
            model_name='champion',
            name='notes',
            field=models.TextField(default=datetime.datetime(2015, 7, 3, 1, 32, 58, 869478, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='date_played',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
        ),
    ]
