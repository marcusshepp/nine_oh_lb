from datetime import date

from django.db import models

from nine_oh_lb.settings import CHAMPION_NAMES as cn


class Team(models.Model):
	""" 
	Anything associated with the enemy team.
	Opposite of `AllyTeam`. 
	"""

	class Meta:
		abstract = True

	kill = models.PositiveIntegerField()
	dragon = models.PositiveIntegerField()
	baron = models.PositiveIntegerField()
	tower = models.PositiveIntegerField()


class Match(models.Model):
	""" # """

	lanes = (
		('bottom', 'Bottom'),
	    ('mid', 'Mid'),
	    ('jungle', 'Jungle'),
	    ('top', 'Top'),
	)
	creeps = models.PositiveIntegerField()
	kill = models.PositiveIntegerField()
	death = models.PositiveIntegerField()
	assist = models.PositiveIntegerField()
	tower = models.PositiveIntegerField()
	first_blood = models.BooleanField(default=False)
	champion = models.PositiveIntegerField()	
	gold_earned = models.PositiveIntegerField()
	killing_spree = models.PositiveIntegerField()
	largest_multikill = models.PositiveIntegerField()
	dmg_to_champions  = models.PositiveIntegerField()
	ward_placed = models.PositiveIntegerField()
	winner = models.BooleanField(default=False)
	creeps_per_min = models.DecimalField(decimal_places=1, max_digits=120)
	items = models.CommaSeparatedIntegerField(max_length=1000)
	lane = models.CharField(max_length=6, choices=lanes)
	lane_opponent = models.PositiveIntegerField()


class QuickGame(models.Model):

	""" For quickly logging game info. """

	user_played = models.CharField(max_length=25, choices=cn)
	enemy_laner = models.CharField(max_length=25, choices=cn)
	enemy_jungler = models.CharField(max_length=25, choices=cn)
	winner = models.BooleanField(default=False)
	date_played = models.DateField(("Date"), default=date.today, null=True)
	note = models.TextField(max_length=250, blank=True)