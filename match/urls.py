"""match URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import Index, CreateGame

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^create-game/$', CreateGame.as_view(), name="create_game"),
]
