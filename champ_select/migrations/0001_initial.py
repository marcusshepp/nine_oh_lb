# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('win', models.PositiveIntegerField()),
                ('loss', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('favorite', models.BooleanField()),
                ('all_time_cs', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lane', models.CharField(max_length=6, choices=[(b'bottom', b'Bottom'), (b'mid', b'Mid'), (b'jungle', b'Jungle'), (b'top', b'Top')])),
                ('win', models.BooleanField(default=False)),
                ('cs', models.PositiveIntegerField()),
                ('first_blood', models.BooleanField(default=False)),
                ('confidence_level', models.IntegerField(null=True, blank=True)),
                ('champion', models.ForeignKey(to='champ_select.Champion')),
            ],
        ),
    ]
