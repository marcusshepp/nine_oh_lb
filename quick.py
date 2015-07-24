import sys
import os
import csv
from datetime import date

from django.conf import settings
settings.configure()

from match.models import QuickGame

def handle(*args, **options):
	if "export" in args:
		games = QuickGame.objects.all()
		file_name = "quick-games-{}.csv".format(date.today())
		path = os.path.join("match/fixtures/", file_name)
		with open(path, 'w') as f:
			try:
				writer = csv.writer(f)
				for g in games:
					writer.writerow(
						(g.user_played, g.enemy_laner, g.enemy_jungler, g.winner, g.date_played, g.note))
			finally:
				f.close()
		print path
	elif "import" in args:
		try:
			path = args[1]
			with csv.reader(str(path)) as f:
				for row in f:
					game = {}
					game["user_played"] = row[0]
					game["enemy_laner"] = row[1]
					game["enemy_jungler"] = row[2]
					game["winner"] = row[3]
					game["date_played"] = row[4]
					game["note"] = row[4]
					QuickGame.objects.create(**game)
		except IndexError:
			print "provide path to data"
	else: print "use args -- `import` or `export`"

handle(sys.argv)