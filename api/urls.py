
"""match URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	APICSPerMin,
	APIKills,
	APIFullGame,
	APIFullChampion,
)

urlpatterns = [
    url(r'^games/$', APICSPerMin.as_view()),
    url(r'^fullgame/$', APIFullGame.as_view()),
    url(r'^kills/$', APIKills.as_view()),
    url(r'^leblanc/$', APIFullChampion.as_view())
]
