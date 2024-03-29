"""
match URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	Index,
	CreateGame,
	AvailableGames,
	AvailableChamps,
	GameDetail,
	CreateGeniusGameData,
)

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^create-game/$', CreateGame.as_view(), name="create_game"),
    url(r'^games/$', AvailableGames.as_view(), name="games"),
    url(r'^champs/$', AvailableChamps.as_view(), name="champs"),
    url(r'^game/(?P<pk>[0-9]+)/$', GameDetail.as_view(), name="game"),
    url(r'^genius/create/$', CreateGeniusGameData.as_view(), name="create_genius"),
]
