from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from pyblanc.lbonevnine.lbonevnine import summoner_id


class PyManager(models.Model):
	""" Extent Django's user just to add the id param to use for pyblanc. """
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	league_server_id = models.PositiveIntegerField(null=True, blank=True)

	def save(self, *args, **kwargs):
		self.league_server_id = summoner_id(
			str(self.user.username))
		super(PyManager, self).save(*args, **kwargs)