from datetime import date

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from nine_oh_lb.settings import (
	CHAMPION_NAMES,
	CHAMPION_STRINGS,
)


class Game(models.Model):
	
	class Meta:
		ordering = ["-date_played"]	
	user = models.ForeignKey(User)
	user_played = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	user_played_fav = models.ForeignKey(
		'FavoriteChampion', 
		related_name="played_saved_champion", 
		blank=True,
		null=True,
		)
	direct_enemy = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	winner = models.BooleanField(default=False)
	date_played = models.DateField(
		("Date"), default=date.today)
	what_you_did_well = models.TextField(max_length=250, blank=True)
	could_have_done_better = models.TextField(max_length=250, blank=True)
	
	def get_absolute_url(self):
		return reverse('game', kwargs={'pk': self.pk})

	def note_prev(self):
		note_prev = self.what_you_did_well[:3]
		return note_prev

	def direct_enemy_prev(self):
		direct_enemy = self.direct_enemy[:3]
		return direct_enemy

	def __unicode__(self):
		return self.get_absolute_url()


class DetailedGame(Game):
	""" For detailed game info. """	
	enemy_jungler = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	enemy_support = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	enemy_top = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	enemy_adc = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	enemy_mid = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	lane = models.CharField(max_length=6, blank=True)
	cs = models.PositiveIntegerField(null=True)
	cs_per_min = models.CommaSeparatedIntegerField(max_length=80)
	xp_per_minute = models.CommaSeparatedIntegerField(max_length=80)
	damage_done = models.PositiveIntegerField(null=True)
	first_blood = models.BooleanField(default=False)
	kill = models.PositiveIntegerField()
	# should be 3 maybe
	kill_participation = models.DecimalField(decimal_places=1, max_digits=120, null=True)
	death = models.PositiveIntegerField()
	assist = models.PositiveIntegerField()
	tower = models.PositiveIntegerField()
	first_blood = models.BooleanField(default=False)
	gold_earned = models.PositiveIntegerField()
	# highest point in game
	killing_spree = models.PositiveIntegerField()
	largest_multikill = models.PositiveIntegerField()
	dmg_to_champions  = models.PositiveIntegerField()
	wards_placed = models.PositiveIntegerField()
	
	def __unicode__(self):
		return self.get_absolute_url()


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

