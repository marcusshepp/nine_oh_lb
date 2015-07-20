# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


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
        migrations.CreateModel(
            name='QuickGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_played', models.CharField(max_length=25, choices=[(266, b'Aatrox'), (103, b'Ahri'), (84, b'Akali'), (12, b'Alistar'), (32, b'Amumu'), (34, b'Anivia'), (1, b'Annie'), (22, b'Ashe'), (268, b'Azir'), (432, b'Bard'), (53, b'Blitzcrank'), (63, b'Brand'), (201, b'Braum'), (51, b'Caitlyn'), (69, b'Cassiopeia'), (31, b"Cho'Gath"), (42, b'Corki'), (122, b'Darius'), (131, b'Diana'), (36, b'Dr. Mundo'), (119, b'Draven'), (245, b'Ekko'), (60, b'Elise'), (28, b'Evelynn'), (81, b'Ezreal'), (9, b'Fiddlesticks'), (114, b'Fiora'), (105, b'Fizz'), (3, b'Galio'), (41, b'Gangplank'), (86, b'Garen'), (150, b'Gnar'), (79, b'Gragas'), (104, b'Graves'), (120, b'Hecarim'), (74, b'Heimerdinger'), (39, b'Irelia'), (40, b'Janna'), (59, b'Jarvan IV'), (24, b'Jax'), (126, b'Jayce'), (222, b'Jinx'), (429, b'Kalista'), (43, b'Karma'), (30, b'Karthus'), (38, b'Kassadin'), (55, b'Katarina'), (10, b'Kayle'), (85, b'Kennen'), (121, b"Kha'Zix"), (96, b"Kog'Maw"), (7, b'LeBlanc'), (64, b'Lee Sin'), (89, b'Leona'), (127, b'Lissandra'), (236, b'Lucian'), (117, b'Lulu'), (99, b'Lux'), (54, b'Malphite'), (90, b'Malzahar'), (57, b'Maokai'), (11, b'Master Yi'), (21, b'Miss Fortune'), (82, b'Mordekaiser'), (25, b'Morgana'), (267, b'Nami'), (75, b'Nasus'), (111, b'Nautilus'), (76, b'Nidalee'), (56, b'Nocturne'), (20, b'Nunu'), (2, b'Olaf'), (61, b'Orianna'), (80, b'Pantheon'), (78, b'Poppy'), (133, b'Quinn'), (33, b'Rammus'), (421, b"Rek'Sai"), (58, b'Renekton'), (107, b'Rengar'), (92, b'Riven'), (68, b'Rumble'), (13, b'Ryze'), (113, b'Sejuani'), (35, b'Shaco'), (98, b'Shen'), (102, b'Shyvana'), (27, b'Singed'), (14, b'Sion'), (15, b'Sivir'), (72, b'Skarner'), (37, b'Sona'), (16, b'Soraka'), (50, b'Swain'), (134, b'Syndra'), (91, b'Talon'), (44, b'Taric'), (17, b'Teemo'), (412, b'Thresh'), (18, b'Tristana'), (48, b'Trundle'), (23, b'Tryndamere'), (4, b'Twisted Fate'), (29, b'Twitch'), (77, b'Udyr'), (6, b'Urgot'), (110, b'Varus'), (67, b'Vayne'), (45, b'Veigar'), (161, b"Vel'Koz"), (254, b'Vi'), (112, b'Viktor'), (8, b'Vladimir'), (106, b'Volibear'), (19, b'Warwick'), (62, b'Wukong'), (101, b'Xerath'), (5, b'Xin Zhao'), (157, b'Yasuo'), (83, b'Yorick'), (154, b'Zac'), (238, b'Zed'), (115, b'Ziggs'), (26, b'Zilean'), (143, b'Zyra')])),
                ('enemy_laner', models.CharField(max_length=25, choices=[(266, b'Aatrox'), (103, b'Ahri'), (84, b'Akali'), (12, b'Alistar'), (32, b'Amumu'), (34, b'Anivia'), (1, b'Annie'), (22, b'Ashe'), (268, b'Azir'), (432, b'Bard'), (53, b'Blitzcrank'), (63, b'Brand'), (201, b'Braum'), (51, b'Caitlyn'), (69, b'Cassiopeia'), (31, b"Cho'Gath"), (42, b'Corki'), (122, b'Darius'), (131, b'Diana'), (36, b'Dr. Mundo'), (119, b'Draven'), (245, b'Ekko'), (60, b'Elise'), (28, b'Evelynn'), (81, b'Ezreal'), (9, b'Fiddlesticks'), (114, b'Fiora'), (105, b'Fizz'), (3, b'Galio'), (41, b'Gangplank'), (86, b'Garen'), (150, b'Gnar'), (79, b'Gragas'), (104, b'Graves'), (120, b'Hecarim'), (74, b'Heimerdinger'), (39, b'Irelia'), (40, b'Janna'), (59, b'Jarvan IV'), (24, b'Jax'), (126, b'Jayce'), (222, b'Jinx'), (429, b'Kalista'), (43, b'Karma'), (30, b'Karthus'), (38, b'Kassadin'), (55, b'Katarina'), (10, b'Kayle'), (85, b'Kennen'), (121, b"Kha'Zix"), (96, b"Kog'Maw"), (7, b'LeBlanc'), (64, b'Lee Sin'), (89, b'Leona'), (127, b'Lissandra'), (236, b'Lucian'), (117, b'Lulu'), (99, b'Lux'), (54, b'Malphite'), (90, b'Malzahar'), (57, b'Maokai'), (11, b'Master Yi'), (21, b'Miss Fortune'), (82, b'Mordekaiser'), (25, b'Morgana'), (267, b'Nami'), (75, b'Nasus'), (111, b'Nautilus'), (76, b'Nidalee'), (56, b'Nocturne'), (20, b'Nunu'), (2, b'Olaf'), (61, b'Orianna'), (80, b'Pantheon'), (78, b'Poppy'), (133, b'Quinn'), (33, b'Rammus'), (421, b"Rek'Sai"), (58, b'Renekton'), (107, b'Rengar'), (92, b'Riven'), (68, b'Rumble'), (13, b'Ryze'), (113, b'Sejuani'), (35, b'Shaco'), (98, b'Shen'), (102, b'Shyvana'), (27, b'Singed'), (14, b'Sion'), (15, b'Sivir'), (72, b'Skarner'), (37, b'Sona'), (16, b'Soraka'), (50, b'Swain'), (134, b'Syndra'), (91, b'Talon'), (44, b'Taric'), (17, b'Teemo'), (412, b'Thresh'), (18, b'Tristana'), (48, b'Trundle'), (23, b'Tryndamere'), (4, b'Twisted Fate'), (29, b'Twitch'), (77, b'Udyr'), (6, b'Urgot'), (110, b'Varus'), (67, b'Vayne'), (45, b'Veigar'), (161, b"Vel'Koz"), (254, b'Vi'), (112, b'Viktor'), (8, b'Vladimir'), (106, b'Volibear'), (19, b'Warwick'), (62, b'Wukong'), (101, b'Xerath'), (5, b'Xin Zhao'), (157, b'Yasuo'), (83, b'Yorick'), (154, b'Zac'), (238, b'Zed'), (115, b'Ziggs'), (26, b'Zilean'), (143, b'Zyra')])),
                ('note', models.TextField(max_length=250, blank=True)),
                ('enemy_jungler', models.CharField(max_length=25, choices=[(266, b'Aatrox'), (103, b'Ahri'), (84, b'Akali'), (12, b'Alistar'), (32, b'Amumu'), (34, b'Anivia'), (1, b'Annie'), (22, b'Ashe'), (268, b'Azir'), (432, b'Bard'), (53, b'Blitzcrank'), (63, b'Brand'), (201, b'Braum'), (51, b'Caitlyn'), (69, b'Cassiopeia'), (31, b"Cho'Gath"), (42, b'Corki'), (122, b'Darius'), (131, b'Diana'), (36, b'Dr. Mundo'), (119, b'Draven'), (245, b'Ekko'), (60, b'Elise'), (28, b'Evelynn'), (81, b'Ezreal'), (9, b'Fiddlesticks'), (114, b'Fiora'), (105, b'Fizz'), (3, b'Galio'), (41, b'Gangplank'), (86, b'Garen'), (150, b'Gnar'), (79, b'Gragas'), (104, b'Graves'), (120, b'Hecarim'), (74, b'Heimerdinger'), (39, b'Irelia'), (40, b'Janna'), (59, b'Jarvan IV'), (24, b'Jax'), (126, b'Jayce'), (222, b'Jinx'), (429, b'Kalista'), (43, b'Karma'), (30, b'Karthus'), (38, b'Kassadin'), (55, b'Katarina'), (10, b'Kayle'), (85, b'Kennen'), (121, b"Kha'Zix"), (96, b"Kog'Maw"), (7, b'LeBlanc'), (64, b'Lee Sin'), (89, b'Leona'), (127, b'Lissandra'), (236, b'Lucian'), (117, b'Lulu'), (99, b'Lux'), (54, b'Malphite'), (90, b'Malzahar'), (57, b'Maokai'), (11, b'Master Yi'), (21, b'Miss Fortune'), (82, b'Mordekaiser'), (25, b'Morgana'), (267, b'Nami'), (75, b'Nasus'), (111, b'Nautilus'), (76, b'Nidalee'), (56, b'Nocturne'), (20, b'Nunu'), (2, b'Olaf'), (61, b'Orianna'), (80, b'Pantheon'), (78, b'Poppy'), (133, b'Quinn'), (33, b'Rammus'), (421, b"Rek'Sai"), (58, b'Renekton'), (107, b'Rengar'), (92, b'Riven'), (68, b'Rumble'), (13, b'Ryze'), (113, b'Sejuani'), (35, b'Shaco'), (98, b'Shen'), (102, b'Shyvana'), (27, b'Singed'), (14, b'Sion'), (15, b'Sivir'), (72, b'Skarner'), (37, b'Sona'), (16, b'Soraka'), (50, b'Swain'), (134, b'Syndra'), (91, b'Talon'), (44, b'Taric'), (17, b'Teemo'), (412, b'Thresh'), (18, b'Tristana'), (48, b'Trundle'), (23, b'Tryndamere'), (4, b'Twisted Fate'), (29, b'Twitch'), (77, b'Udyr'), (6, b'Urgot'), (110, b'Varus'), (67, b'Vayne'), (45, b'Veigar'), (161, b"Vel'Koz"), (254, b'Vi'), (112, b'Viktor'), (8, b'Vladimir'), (106, b'Volibear'), (19, b'Warwick'), (62, b'Wukong'), (101, b'Xerath'), (5, b'Xin Zhao'), (157, b'Yasuo'), (83, b'Yorick'), (154, b'Zac'), (238, b'Zed'), (115, b'Ziggs'), (26, b'Zilean'), (143, b'Zyra')])),
                ('winner', models.BooleanField(default=False)),
                ('date_played', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
            ],
        ),
    ]
