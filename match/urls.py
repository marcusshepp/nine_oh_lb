"""match URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	Index,
	CreateGame,
	AvailableGames,
	GameDetail,
	Genius,
	CreateGeniusGameData,
	APICSPerMin,
	APIKills,
	APIFullGame,
	APIFullChampion,
)

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^create-game/$', CreateGame.as_view(), name="create_game"),
    url(r'^games/$', AvailableGames.as_view(), name="games"),
    url(r'^game/(?P<pk>[0-9]+)/$', GameDetail.as_view(), name="game"),
    url(r'^genius/$', Genius.as_view(), name="genius"),
    url(r'^genius/create/$', CreateGeniusGameData.as_view(), name="create_genius"),
    url(r'^api/games/$', APICSPerMin.as_view()),
    url(r'^api/fullgame/$', APIFullGame.as_view()),
    url(r'^api/kills/$', APIKills.as_view()),
    url(r'^api/leblanc/$', APIFullChampion.as_view())
]
