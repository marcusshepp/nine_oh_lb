from datetime import date

from django.test import TestCase

from champ_select.models import (
		Game,
		Champion,
		EnemyChampion,
	)


class ChampSelectTestCase(TestCase):
	"""
	Creates `Game(s)` then quickly deletes them.
	"""

	def setUp(self):
		champion = {
			"name": 7, # Leblanc
			"notes": "Note about `Leblanc`.",
			"date_created": date.today(),
		}
		enemy = {
			"name": "Leblanc",
		}
		Champion.objects.create(**champion)
		EnemyChampion.objects.create(**enemy)

	def test_champion_exists(self):
		c = Champion.objects.all().filter(name=7).exists()
		self.assertTrue(c) # Champion exists

	def test_enemy_champion_exists(self):
		ec = EnemyChampion.objects.all().filter(name="Leblanc").exists()
		self.assertTrue(ec)

	def test_creation_and_exists_game(self):
		champ = Champion.objects.get(pk=1)
		ec = EnemyChampion.objects.get(pk=1)
		data = {
			"champion": champ,
			"enemy_laner": ec,
			"lane": "Mid",
			"win": True,
			"cs": 500,
			"damage_done": 50000,
			"first_blood": True,
			"date_played": date.today(),
		}
		Game.objects.create(**data)
		g = Game.objects.all().filter(date_played=date.today()).exists()
		self.assertTrue(g)