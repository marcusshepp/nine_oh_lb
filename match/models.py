from datetime import date

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from nine_oh_lb.settings import (
	CHAMPION_NAMES,
	CHAMPION_STRINGS,
)


class Game(models.Model):

	user = models.ForeignKey(User)
	user_played = models.CharField(
		max_length=25, choices=CHAMPION_NAMES)
	user_played_fav = models.ForeignKey(
		'FavoriteChampion', 
		related_name="played_saved_champion", 
		blank=True,
		null=True,
		)
	direct_enemy = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True, null=True)
	winner = models.BooleanField(default=False)
	what_you_did_well = models.TextField(max_length=250, blank=True, null=True)
	could_have_done_better = models.TextField(max_length=250, blank=True, null=True)
	enemy_jungler = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True, null=True)
	enemy_support = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True, null=True)
	enemy_top = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True, null=True)
	enemy_adc = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True, null=True)
	enemy_mid = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True, null=True)
	lane = models.CharField(max_length=6, blank=True, null=True)
	cs = models.PositiveIntegerField(null=True, blank=True)
	cs_per_min = models.CommaSeparatedIntegerField(max_length=80, blank=True, null=True)
	xp_per_minute = models.CommaSeparatedIntegerField(max_length=80, blank=True, null=True)
	damage_done = models.PositiveIntegerField(null=True, blank=True)
	first_blood = models.BooleanField(default=False)
	kill = models.PositiveIntegerField(blank=True, null=True)
	# should be 3 maybe
	kill_participation = models.DecimalField(decimal_places=1, max_digits=120, null=True, blank=True)
	death = models.PositiveIntegerField(blank=True, null=True)
	assist = models.PositiveIntegerField(blank=True, null=True)
	tower = models.PositiveIntegerField(blank=True, null=True)
	first_blood = models.BooleanField(default=False)
	gold_earned = models.PositiveIntegerField(blank=True, null=True)
	# highest point in game
	killing_spree = models.PositiveIntegerField(blank=True, null=True)
	largest_multikill = models.PositiveIntegerField(blank=True, null=True)
	dmg_to_champions  = models.PositiveIntegerField(blank=True, null=True)
	wards_placed = models.PositiveIntegerField(blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse('game', kwargs={'pk': self.pk})

	def note_prev(self):
		note_prev = self.what_you_did_well[:3]
		return note_prev

	def direct_enemy_prev(self):
		direct_enemy = self.direct_enemy[:3]
		return direct_enemy

	def display_winner(self):
		if self.winner:
			return "Win"
		else:
			return "Lose"

	def __unicode__(self):
		return "{}".format(self.user_played)


class TeamStats(models.Model):
	""" ally team stats, used for comparison to user. """
	kill = models.PositiveIntegerField()
	dragon = models.PositiveIntegerField()
	baron = models.PositiveIntegerField()
	tower = models.PositiveIntegerField()
	date_played = models.DateField(
		("Date"), default=date.today)


class FavoriteChampion(models.Model):

	user = models.ForeignKey(User)
	name = models.CharField(
		max_length=25, choices=CHAMPION_NAMES)
	games = models.ManyToManyField(
		Game, 
		blank=True, 
		)

	def __unicode__(self):
		return u"{}".format(
			self.name,
		)

	def create_from_games(self):
		games = Game.objects.filter(user_played__icontains=self.name)
		if games:
			for g in games:
				self.games.add(g)
			return True
		return False

