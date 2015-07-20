import csv
from datetime import date

from django.core.management.base import BaseCommand

from match.models import QuickGame

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		games = QuickGame.objects.all()
		f = open("match/fixtures/quick-games-{}.csv".format(date.today()), 'wt')
		try:
			writer = csv.writer(f)
			for g in games:
				writer.writerow(
					(g.user_played, g.enemy_laner, g.enemy_jungler, g.winner, g.date_played, g.note))
		finally:
			f.close()
		print open("match/fixtures/quick-games-{}.csv".format(date.today()), 'rt')