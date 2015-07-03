# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creeps', models.PositiveIntegerField()),
                ('kill', models.PositiveIntegerField()),
                ('death', models.PositiveIntegerField()),
                ('assist', models.PositiveIntegerField()),
                ('tower', models.PositiveIntegerField()),
                ('first_blood', models.BooleanField(default=False)),
                ('champion', models.PositiveIntegerField()),
                ('gold_earned', models.PositiveIntegerField()),
                ('killing_spree', models.PositiveIntegerField()),
                ('largest_multikill', models.PositiveIntegerField()),
                ('dmg_to_champions', models.PositiveIntegerField()),
                ('ward_placed', models.PositiveIntegerField()),
                ('winner', models.BooleanField(default=False)),
                ('creeps_per_min', models.DecimalField(max_digits=120, decimal_places=1)),
                ('items', models.CommaSeparatedIntegerField(max_length=1000)),
                ('lane', models.CharField(max_length=6, choices=[(b'bottom', b'Bottom'), (b'mid', b'Mid'), (b'jungle', b'Jungle'), (b'top', b'Top')])),
                ('lane_opponent', models.PositiveIntegerField()),
            ],
        ),
    ]
