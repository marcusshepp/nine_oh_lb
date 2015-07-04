from os import path
from datetime import date

from django.core.management.base import BaseCommand

from champ_select.frontalcortex import League
from nine_oh_lb.settings_lite import MATCH_FIXTURES_URL


class Command(BaseCommand):

	l = League()
	td = date.today()
	error_message = "Already have data for today."

	def handle(self, *args, **kwargs):
		possible_file = "{0}{1}.json".format(MATCH_FIXTURES_URL, self.td)
		if path.isfile(possible_file):
			return self.error_message
		return l.stats_to_file(self.relative_path, self.td) # works!
