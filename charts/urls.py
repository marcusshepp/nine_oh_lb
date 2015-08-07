"""charts URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	Genius,
	APICSPerMin,
	APIKills,
	APIFullGame,
	APIChampionDMG,
	ChampionDMG,
	APIGamesPlayedTopFive,
	TopFiveChampionsPlayed,
)

urlpatterns = [
    url(r'^$', Genius.as_view(), name="genius"),
    url(r'^games/$', APICSPerMin.as_view()),
    url(r'^fullgame/$', APIFullGame.as_view()),
    url(r'^kills/$', APIKills.as_view()),
    url(r'^json-dmg/$', APIChampionDMG.as_view(), name="json_dmg"),
    url(r'^dmg/$', ChampionDMG.as_view(), name="dmg"),
    url(r'^json-top-five/$', APIGamesPlayedTopFive.as_view(), name="json_top_five"),
    url(r'^top-five/$', TopFiveChampionsPlayed.as_view(), name="top_five")
]
