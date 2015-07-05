from os import path
from datetime import date

from django.core.management.base import BaseCommand

from champ_select.models import Champion, EnemyChampion
from nine_oh_lb.settings_lite import CHAMPION_NAMES


class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		for name in CHAMPION_NAMES:
			Champion.objects.get_or_create(name=name)
			EnemyChampion.objects.get_or_create(name=name)
		num = len(Champion.objects.all())
		return "{} champions in DB.".format(num)