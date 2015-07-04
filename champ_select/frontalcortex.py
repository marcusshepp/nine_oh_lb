# Frontal Cortext of this Thinking Machine.
# Communicates with League Server and retrieves Information for its user.
# Author: Marcus Shepherd

import os
import json
import math
import urllib2 as urll


class League(object):
    """ 
    This obj retreives match history information for Marcus Shepherd. 
    Current Account: marcusshep
    """

    def __unicode__(self, summoner=42008349):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"{}".format(summoner)

    def server_request(self):
        """ Makes a request to League servers and returns parsed JSON data."""
        api_key = "8a9d2c2d-f00d-406b-87b1-810c2312a1ae"
        url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/%s?api_key=%s" % (marcusshep, api_key)
        request = urll.urlopen(url)
        parsed = json.loads(request.read())
        return parsed
    
    def stats_to_file(self):
        """ Writes a Python dictionary of League Stats to a file. """
        parsed = self.server_request()
        if os.path.isfile(mh):
                os.remove(mh)
                with open(mh, "w") as text:
                    text.write(json.dumps(parsed, indent=4, sort_keys=True))
    
    def read_data_from_file(self):
        """ Returns parsed data from a file. """
        with open("match_history.json", "r") as data_file:
            parsed = json.load(data_file)
        return parsed

    def pretty_stats(self):
        """ Returns a pretty formatted dict. """
        parsed = self.server_request()
        return json.dumps(parsed, indent=4, sort_keys=True)

    def get_stat(self, game_number, stat_name):
        """ Returns a stat """
    	parsed = self.server_request()
        # parsed = self.read_data_from_file()
    	return parsed['matches'][game_number]['participants'][0]['stats'][stat_name]

    def get_average_creep_score(self):
        """ Returns the average creep score for the last ten games. """
        total = []
        total_creep_count = 0
        for i in range(0, 10):
            total.append(self.get_stat(int(i), "minionsKilled"))
        for j in range(0, len(total)):
            total_creep_count+=total[j]
        return total_creep_count/10
    
    def get_creep_plt_data(self):
        """ Returns an array that can be used with matplotlib for data visualization. """
        scores = []
        for i in range(0, 10):
            scores.append(self.get_stat(int(i), "minionsKilled"))
        return scores
    
    def get_win_lose(self):
        """ Returns the win/lose ratio. """ 
        counter, num_of_wins, num_of_lose = 0, 0, 0
        for i in range(0, 10):
            if self.get_stat(int(i), "winner") == True:
                num_of_wins += 1
            else:
                num_of_lose += 1
        return math.ceil(num_of_lose/num_of_wins)
