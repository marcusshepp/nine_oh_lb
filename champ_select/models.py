from __future__ import division
from datetime import date

from django.db import models

from .frontalcortex import League


class Champion(models.Model):
	""" 
	Dished to `User` during `champ_select` depending on `Game`.
	"""

	name = models.CharField(max_length=25)
	notes = models.TextField(max_length=1000)
	games = models.ManyToManyField("Game", related_name="games_played_with")
	date_created = models.DateField(("Date"), default=date.today)

	def __unicode__(self):
		""" Display `name`. """
		return u"{}".format(self.name)
	
	def get_games(self):
		if self.games:
			games = Game.objects.filter(champion=self.id)
			return games

	def number_of_games(self):
		if self.games:
			return len(self.get_games())

	def average_cs(self):
		if self.number_of_games() > 0:
			v = 0
			i = self.get_games()
			for _ in i:
				v += _.cs
			j = v / self.number_of_games()
			return j


class EnemyChampion(models.Model):
	"""
	Stores info about the enemy team.
	"""
	name = models.CharField(max_length=25)

	def __unicode__(self):
		""" Display `name`. """
		return u"{}".format(self.name)


class Game(models.Model):
	""" 
	A game is played by a `User`. 
	Each game is played with a different `Champion`.
	"""
	lanes = (
		('bottom', 'Bottom'),
	    ('mid', 'Mid'),
	    ('jungle', 'Jungle'),
	    ('top', 'Top'),
	)
	champion = models.ForeignKey(Champion, related_name="champion_used_for_game")
	enemy_laner = models.ForeignKey(
		EnemyChampion, null=True, blank=True, related_name="champion_played_against")
	lane = models.CharField(max_length=6, choices=lanes)
	win = models.BooleanField(default=False)
	cs = models.PositiveIntegerField(null=True)
	damage_done = models.PositiveIntegerField(null=True)
	first_blood = models.BooleanField(default=False)
	date_played = models.DateField(("Date"), default=date.today)

	def __unicode__(self):
		""" Display `Champion` name. """
		display = self.champion
		return u"{}".format(display)

	def game_quick_info(self):
		""" Returns a str of information about the game. """
		if self.enemy_laner:
			return u"{0} vs. {1}".format(self.champion, self.enemy_laner)
