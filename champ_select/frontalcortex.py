# Frontal Cortext of this Thinking Machine.
# Communicates with League Server and retrieves information for its user.
# Author: Marcus Shepherd

import os
import json
import math
import urllib2 as urll
from datetime import date

import pandas as pd
import numpy as np


class League(object):

    """
    Do NOT instantiate this class itself.
    Only instantiate League's subclasses.
    """

    marcusshep = 42008349
    summoner = marcusshep
    api_key = "8a9d2c2d-f00d-406b-87b1-810c2312a1ae"
    settings = {}

    def __init__(self):
        """ Initialize obj with debug = False """
        
    def __unicode__(self):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"{}".format(self.summoner)

    @staticmethod
    def get_request(url, api_key=api_key):
        url += "?api_key={0}".format(api_key)
        request = urll.urlopen(url)
        parsed = json.loads(request.read())
        return parsed

    @classmethod
    def match_history_request(self):
        """ Makes a request to League servers and returns parsed JSON data."""
        url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{0}".format(self.summoner)
        return self.get_request(url)

    def champion_list(self):
        url = "https://na.api.pvp.net/api/lol/na/v1.2/champion"
        return self.get_request(url)
    

class LeagueFile(League):

    """
    Class for reading/writing League stats to/from files.
    """
    
    path_to_data = "champ_select/fixtures/" # relativate to django's manage.py
    # path_to_data = "fixtures/" # relativate to pycharm interperter

    def stats_from_file(self):
        """ Returns numpy array of data from a file. """
        # an absolute path to folder containing JSON.
        path = r'{}'.format(self.path_to_data)  
        for dir_entry in os.listdir(path):
            dir_entry_path = os.path.join(path, dir_entry)
            if os.path.isfile(dir_entry_path):
                with open(dir_entry_path) as my_file:
                    data = json.load(my_file)
        if data:
            return data['matches'] # rid myself of this layer
        return None
    
    def stats_to_file(self, relative_path):
        """ Writes match history to a file in a given location. """
        parsed, file_name = self.match_history_request(), date.today()
        complete_path = os.path.abspath("{0}{1}.json".format(relative_path, file_name))
        if os.path.isfile(complete_path):
            file_name = "{}-duplicate".format(date.today())
            complete_path = os.path.abspath("{0}{1}.json".format(relative_path, file_name))
        with open(complete_path, "w") as f:
            f.write(json.dumps(parsed))
            f.close()
        return str(complete_path)
    

class LeagueStat(League):

    """ 
    Handles the `Stat` data field. 
    Available methods:
        get_stat
        all_minions_killed
        average_cs
        winoverlose
        get_champion_id
        all_champion_ids
    """
     
    def get_stat(self, game_number, stat_name):
        """ Returns a stat """
        parsed = self.match_history_request()
        return parsed['matches'][game_number]['participants'][0]['stats'][stat_name]
        
    def all_minions_killed(self):
        """ Returns an array that can be used for data visualization. """
        scores = []
        for i in xrange(10):
            scores.append(self.get_stat(int(i), "minionsKilled"))
        return scores

    def average_cs(self):
        """ Returns the average creep score for the last ten games. """
        total = []
        total_creep_count = 0
        for i in xrange(10):
            total.append(self.get_stat(int(i), "minionsKilled"))
        for j in range(0, len(total)):
            total_creep_count+=total[j]
        return total_creep_count/10

    def winoverlose(self):
        """ Returns the win/lose ratio. """ 
        counter, num_of_wins, num_of_lose = 0, 0, 0
        for i in xrange(10):
            if self.get_stat(int(i), "winner") == True:
                num_of_wins += 1
            else:
                num_of_lose += 1
        return math.ceil(num_of_lose/num_of_wins)
    
    def get_champion_id(self, game_number):
        parsed = self.match_history_request()
        return parsed['matches'][game_number]['participants'][0]['championId']
    
    def all_champion_ids(self):
        list_of_champion_ids = []
        for game_number in xrange(10):
            list_of_champion_ids.append(self.get_champion_id(game_number))
        return list_of_champion_ids


class LeagueTimelineR(League):


    def timeline_request(self, game_number, stat_name, *args, **kwargs):
        """ Returns the `timeline` data, type: dict. """
        parsed = self.match_history_request(marcusshep)
        return parsed['matches'][game_number]['participants'][0]['timeline'][stat_name]


class Timeline(LeagueFile):

    """
    Handles the `timeline` dict. Data is per minute.
    Available methods:
        timeline_request
        timeline_file
        timeline_lanes
        timeline_cspermin
        timeline_cspermin_bytime
        timeline_xppermin
    """

    def timeline_file(self, stat_name, *args, **kwargs):
        """ Returns the `timeline` data for a given stat, type: dict. """
        matches = self.stats_from_file()
        timeline = {}
        for n in xrange(10):
            timeline[n] = matches[n]['participants'][0]['timeline'][stat_name]
        return timeline
    
    def timeline_lanes(self):
        """ Returns game lane value for `game_number`.  """
        lanes = self.timeline_file("lane")
        for g, l in lanes.iteritems():
            lanes[g] = str(l) # from unicode to str
        return lanes # {game_num: 'lane'}

    def timeline_xp(self):
        dict_of_values = self.timeline_file("xpPerMinDeltas")
        return dict_of_values

    def timeline_cs(self, time_value=None):
        """ 
        cspermin from 0 to 30 min.
        `time_value` can be: 
        zeroToTen
        tenToTwenty
        twentyToThirty
        """
        time_value = str(time_value)
        data = self.timeline_file("creepsPerMinDeltas")
        df = pd.DataFrame(data) # pandas
        return df

    def timeline_averagecs(self):
        """
        :return:
        list of float64 containing average cspermin.
        """
        df = self.timeline_cs()
        df = df.apply(lambda x: x.max() - x.min())
        return df

    def judge_cs(self):
        df = self.timeline_averagecs()
        maxx = df.max()
        choices = [
            "challenger",
            "master",
            "diamond",
            "platinum",
            "gold",
            "silver"
            "bronze",
        ]
        v = ""
        # if  7 <= maxx <= 8:
        #     v += choices[0]
        # elif  6 <= maxx <= 7:
        #     v += choices[1]
        # elif  5 <= maxx <= 6:
        #     v += choices[2]
        # elif  4 <= maxx <= 5:
        #     v += choices[3]
        # elif  3 <= maxx <= 4:
        #     v += choices[4]
        # elif  2 <= maxx <= 3:
        #     v += choices[5]
        # elif  0 <= maxx <= 2:
        #     v += choices[6]

        
#         return pd.DataFrame(df, index=choices)





# tl = Timeline()
# print tl.judge_cs()

# ls = LeagueStat()
# print ls.average_cs()
