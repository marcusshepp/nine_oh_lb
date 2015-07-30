import os
import json
import math
import requests
import requests_cache


requests_cache.install_cache(
    'stat_cache', backend="memory", expire_after=3600) #one hour


class BackEnd(object):
    """
    Do NOT instantiate this class itself.
    Only instantiate League's subclasses.
    """

    api_key = ""
    summoner = 0

    def __init__(self, api_key, summoner):
        """ Initialize obj with debug = False """
        self.api_key = api_key
        self.summoner = summoner

    def __unicode__(self):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"PyBlanc object instance. Summoner: {}".format(self.summoner)

    def get_data(self):
        """ 
        Makes a request to League servers and returns parsed JSON data.
        If called within same hour, retrieves data from memory cache.
        """
        url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{0}".format(self.summoner)
        url += "?api_key={0}".format(self.api_key)
        request = requests.get(url)
        parsed = request.json()
        return parsed