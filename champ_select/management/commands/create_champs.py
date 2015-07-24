from os import path
from datetime import date

from django.core.management.base import BaseCommand

from champ_select.models import EnemyChampion
from nine_oh_lb.settings_lite import CHAMPION_NAMES


class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		for champ in CHAMPION_NAMES:
			EnemyChampion.objects.get_or_create(name=str(champ[1]))
		num = len(EnemyChampion.objects.all())
		return "{0} EnemyChampion objects in DB.".format(num)