from datetime import date

from django.db import models


class Champion(models.Model):
	""" 
	Dished to `User` during `champ_select` depending on `Game`.
	"""
	
	name = models.CharField(max_length=50)
	notes = models.TextField(max_length=1000)
	games = models.ManyToManyField('Game')
	date_created = models.DateField(("Date"), default=date.today)

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
	lane = models.CharField(max_length=6, choices=lanes)
	win = models.BooleanField(default=False)
	cs = models.PositiveIntegerField()
	first_blood = models.BooleanField(default=False)
	confidence_level = models.IntegerField(null=True, blank=True)
	date_played = models.DateField(("Date"), default=date.today)