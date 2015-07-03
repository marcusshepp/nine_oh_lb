from datetime import date

from django.db import models

from .frontalcortex import LeagueStats


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

	# def get_stat_from_server(self, stat, *args, **kwargs):
	# 	ls = LeagueStats()
	# 	return ls.get_stat(stat)

	# def create_objects(self):
	# 	exist = self.objects.all()

	# 	for e in exist:
	# 		if 

	# def get_win_booleans(self):
	# 	""" 
	# 	Returns all `games` played by a perticular `champion`. 
	# 	"""
	# 	return "\n".join([g.win for g in self.games.all()])

	# def get_average_cs(self):
	# 	"""
	# 	Returns average creepscore(cs).
	# 	"""
	# 	total_cs = 0
	# 	games = self.games.objects.all()
	# 	for g in games:
	# 		total_cs += g.cs
	# 	return total_cs / games


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




