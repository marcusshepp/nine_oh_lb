from datetime import date

from django.db import models

from nine_oh_lb.settings import (
	CHAMPION_NAMES,
	CHAMPION_STRINGS,
)


class QuickGame(models.Model):

	""" For quickly logging game info. """

	user_played = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	user_played_fav = models.ForeignKey(
		'FavoriteChampion', 
		related_name="played_saved_champion", 
		blank=True,
		null=True,
		)
	enemy_laner = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	enemy_jungler = models.CharField(
		max_length=25, choices=CHAMPION_NAMES, blank=True)
	winner = models.BooleanField(default=False)
	date_played = models.DateField(
		("Date"), default=date.today, null=True)
	note = models.TextField(max_length=250, blank=True)
	
	def __unicode__(self):
		p = ""
		if self.user_played:
			p += self.user_played
		else: p += self.user_played_fav.name
		return u"{0} vs. {1}".format(
			p, 
			self.enemy_laner
		)


class FavoriteChampion(models.Model):

	name = models.CharField(
		max_length=25, choices=CHAMPION_NAMES)
	games = models.ManyToManyField(
		QuickGame, 
		blank=True, 
		)

	def __unicode__(self):
		return u"{}".format(
			self.name,
		)

	def create_from_games(self):
		games = QuickGame.objects.filter(user_played__icontains=self.name)
		if games:
			for g in games:
				self.games.add(g)
			return True
		return False

	def save(self):
		self.save()
		self.create_from_games()
		self.save()
		return self