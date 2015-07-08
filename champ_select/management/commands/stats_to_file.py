from os import path
from datetime import date

from django.core.management.base import BaseCommand

from champ_select.frontalcortex import LeagueFile
from nine_oh_lb.settings_lite import MATCH_FIXTURES_URL


class Command(BaseCommand):

	lf = LeagueFile(settings=True)
	td = date.today()
	error_message = "File exists, proceed? [y/n] "
	abort = "Abort!"

	def handle(self, *args, **kwargs):
		complete_path = "{}{}.json".format(MATCH_FIXTURES_URL, self.td)
		if path.isfile(complete_path):
			boo = raw_input("{}".format(self.error_message))
			if boo == "no" or boo == "n":
				return "{}".format(self.abort)
		return "Created file at: {}".format(self.lf.stats_to_file(MATCH_FIXTURES_URL))
