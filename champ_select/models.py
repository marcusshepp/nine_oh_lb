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
		games = Game.objects.filter(champion=self.id)
		return games

	def number_of_games(self):
		return len(self.get_games())

	def average_cs(self):
		v = 0
		i = self.get_games()
		for _ in i:
			v += _.cs
		j = v / self.number_of_games()
		return j	


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
	champion = models.ForeignKey(Champion)
	lane = models.CharField(max_length=6, choices=lanes)
	win = models.BooleanField(default=False)
	cs = models.PositiveIntegerField(null=True)
	damage_done = models.PositiveIntegerField(null=True)
	first_blood = models.BooleanField(default=False)
	confidence_level = models.IntegerField(null=True, blank=True)
	date_played = models.DateField(("Date"), default=date.today)

	def __unicode__(self):
		""" Display `Champion` name. """
		display = self.champion
		return u"{}".format(display)




