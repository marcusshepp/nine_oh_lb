# list cronjobs: crontab -l 
# create cronjob: crontab -e

from champ_select.frontalcortex import LeagueFile

lf = LeagueFile()
lf.stats_to_file("champ_select/fixtures/")