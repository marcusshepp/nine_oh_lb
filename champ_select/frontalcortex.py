# Frontal Cortext of this Thinking Machine.
# Communicates with League Server and retrieves information for its user.
# Author: Marcus Shepherd

import os
import json
import math
import urllib2 as urll
from datetime import date

import numpy as np


class League(object):

    marcusshep = 42008349
    summoner = marcusshep
    api_key = "8a9d2c2d-f00d-406b-87b1-810c2312a1ae"
    settings = {}

    def __init__(self, settings):
        """ Initialize obj with debug = False """
        self.settings['debug'] = settings
        
    def __unicode__(self, summoner=marcusshep):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"{}".format(summoner)
        
    def get_request(self, url, api_key=api_key):
        url += "?api_key={0}".format(api_key)
        request = urll.urlopen(url)
        parsed = json.loads(request.read())
        return parsed

    def match_history_request(self, summoner):
        """ Makes a request to League servers and returns parsed JSON data."""
        url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{0}".format(summoner)
        return self.get_request(url)

    def champion_list(self):
        url = "https://na.api.pvp.net/api/lol/na/v1.2/champion"
        return self.get_request(url)
    
    def print_stats(self):
        """ Returns a pretty formatted dict. """
        parsed = self.match_history_request()
        return json.dumps(parsed, indent=4, sort_keys=True)


class LeagueFile(League):
    
    path_to_data = ""
    
    def read_data_from_file(self, path):
        """ Returns parsed data from a file. """
        import os
        # an absolute path to folder containing JSON.
        path = r'{}'.format(path)  
        data = {}
        for dir_entry in os.listdir(path):
            dir_entry_path = os.path.join(path, dir_entry)
            if os.path.isfile(dir_entry_path):
                with open(dir_entry_path, 'r') as my_file:
                    data[dir_entry] = my_file.read()
        if data:
            matches = data.itervalues()
            l = []
            for match in matches:
                l.append(match)
            return l
        return None

    def timeline_file_all(self, stat_name, *args, **kwargs):
        """ Returns the `timeline` data, type: dict. """
        path = "../../projects/nine_oh_lb/champ_select/fixtures/"
        parsed = self.read_data_from_file("{}".format(path))
        data = []
        for game_number in range(len(parsed)):
            data.append(parsed['matches'])
            #[game_number]['participants'][0]['timeline'])
        return data
    
    def stats_to_file(self, relative_path, file_name):
        """ Writes match history to a file in a given location. """
        parsed = self.match_history_request(self.summoner)
        file_name = date.today()
        complete_path = os.path.abspath("{0}{1}.json".format(relative_path, file_name))
        with open(complete_path, "w") as text:
            text.write(json.dumps(parsed, indent=4, sort_keys=True))
        return str(complete_path)
    

class LeagueStat(League):
     
    def get_stat(self, game_number, stat_name):
        """ Returns a stat """
        parsed = self.match_history_request(marcusshep)
        return parsed['matches'][game_number]['participants'][0]['stats'][stat_name]
        
    def all_minions_killed(self):
        """ Returns an array that can be used for data visualization. """
        scores = []
        for i in range(0, 10):
            scores.append(self.get_stat(int(i), "minionsKilled"))
        return scores

    def average_cs(self):
        """ Returns the average creep score for the last ten games. """
        total = []
        total_creep_count = 0
        for i in range(0, 10):
            total.append(self.get_stat(int(i), "minionsKilled"))
        for j in range(0, len(total)):
            total_creep_count+=total[j]
        return total_creep_count/10

    def winoverlose(self):
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


class LeagueTimeline(LeagueFile):

    def get_timeline_request(self, game_number, stat_name, *args, **kwargs):
        """ Returns the `timeline` data, type: dict. """
        parsed = self.match_history_request(marcusshep)
        return parsed['matches'][game_number]['participants'][0]['timeline'][stat_name]    
    
    
    def timeline_lane(self, game_number):
        """ Returns game lane value for `game_number`.  """
        lane = str(self.get_timeline_file(game_number, "lane"))
        return lane
    
    def timeline_all_lanes(self):
        """ Last ten games played. """
        list_of_lanes = []
        for game_number in range(10):
            list_of_lanes.append(self.timeline_lane(game_number))
        return list_of_lanes
    
    def timeline_cspermin(self, game_number):
        """ Returns one dict of creeps killed per minute. """
        dict_of_values = self.timeline_file_all(game_number, "creepsPerMinDeltas")
        return dict_of_values

    def timeline_cspermin_all(self):
        all_values = []
        for i in range(10):
            all_values.append(self.timeline_file_all("creepsPerMinDeltas"))
        return all_values
    
    def timeline_xppermin(self, game_number):
        dict_of_values = self.timeline_file_all(game_number, "xpPerMinDeltas")
        return dict_of_values
    