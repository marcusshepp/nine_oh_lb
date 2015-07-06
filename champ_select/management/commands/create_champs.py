from os import path
from datetime import date

from django.core.management.base import BaseCommand

from champ_select.frontalcortex import League
from nine_oh_lb.settings_lite import CHAMPION_NAMES


class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		l = League()
		_list = l.champion_list()
		print _list
		return None