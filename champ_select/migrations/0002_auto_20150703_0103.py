# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champ_select', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='all_time_cs',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='loss',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='win',
        ),
    ]
