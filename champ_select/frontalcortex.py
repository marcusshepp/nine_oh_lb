# Frontal Cortext of this Thinking Machine.
# Communicates with League Server and retrieves information for its user.
# Author: Marcus Shepherd

import os
import json
import math
import urllib2 as urll
from datetime import date

marcusshep = 42008349

class League(object):

    summoner = marcusshep
    api_key = "8a9d2c2d-f00d-406b-87b1-810c2312a1ae"

    def __unicode__(self, summoner=marcusshep):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"{}".format(summoner)

    def get_request(self, url, api_key=api_key):
        url += "?api_key=%s" % api_key
        request = urll.urlopen(url)
        parsed = json.loads(request.read())
        return parsed

    def match_history_request(self, summoner):
        """ Makes a request to League servers and returns parsed JSON data."""
        url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/%s" % (summoner)
        return self.get_request(url)

    def champion_list(self):
        url = "https://na.api.pvp.net/api/lol/na/v1.2/champion"
        return self.get_request(url)

    def stats_to_file(self, relative_path, file_name):
        """ Writes match history to a file in a given location. """
        parsed = self.match_history_request(self.summoner)
        file_name = date.today()
        complete_path = os.path.abspath("%s%s.json") % (relative_path, file_name)
        with open(complete_path, "w") as text:
            text.write(json.dumps(parsed, indent=4, sort_keys=True))
        return str(complete_path)
    
    def read_data_from_file(self):
        """ Returns parsed data from a file. """
        with open("match_history.json", "r") as data_file:
            parsed = json.load(data_file)
        return parsed

    def stats_to_pretty(self):
        """ Returns a pretty formatted dict. """
        parsed = self.match_history_request()
        return json.dumps(parsed, indent=4, sort_keys=True)

    def get_stat(self, game_number, stat_name):
        """ Returns a stat """
        parsed = self.match_history_request(marcusshep)
        return parsed['matches'][game_number]['participants'][0]['stats'][stat_name]
    
    def stat_all_minions_killed(self):
        """ Returns an array that can be used for data visualization. """
        scores = []
        for i in range(0, 10):
            scores.append(self.get_stat(int(i), "minionsKilled"))
        return scores

    def stat_average_cs(self):
        """ Returns the average creep score for the last ten games. """
        total = []
        total_creep_count = 0
        for i in range(0, 10):
            total.append(self.get_stat(int(i), "minionsKilled"))
        for j in range(0, len(total)):
            total_creep_count+=total[j]
        return total_creep_count/10

    def stat_winoverlose(self):
        """ Returns the win/lose ratio. """ 
        counter, num_of_wins, num_of_lose = 0, 0, 0
        for i in range(0, 10):
            if self.get_stat(int(i), "winner") == True:
                num_of_wins += 1
            else:
                num_of_lose += 1
        return math.ceil(num_of_lose/num_of_wins)
    
    def get_champion_id(self, game_number):
        parsed = self.match_history_request(marcusshep)
        return parsed['matches'][game_number]['participants'][0]['championId']
    
    def all_champion_ids(self):
        list_of_champion_ids = []
        for game_number in range(10):
            list_of_champion_ids.append(self.get_champion_id(game_number))
        return list_of_champion_ids
    
    def get_timeline(self, game_number, stat_name, *args, **kwargs):
        """ Returns the `timeline` data, type: dict. """
        parsed = self.match_history_request(marcusshep)
        return parsed['matches'][game_number]['participants'][0]['timeline'][stat_name]
    
    def timeline_lane(self, game_number):
        """ Returns game lane value for `game_number`.  """
        lane = str(self.get_timeline(game_number, "lane"))
        return lane
    
    def timeline_all_lanes(self):
        """ Last ten games played. """
        list_of_lanes = []
        for game_number in range(10):
            list_of_lanes.append(self.timeline_lane(game_number))
        return list_of_lanes
    
    def timeline_cspermin(self, game_number):
        """ Returns one dict of creeps killed per minute. """
        dict_of_values = self.get_timeline(game_number, "creepsPerMinDeltas")
        return dict_of_values
    
    def timeline_xppermin(self, game_number):
        dict_of_values = self.get_timeline(game_number, "xpPerMinDeltas")
        return dict_of_values