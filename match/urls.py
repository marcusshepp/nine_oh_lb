"""match URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import Index

urlpatterns = [
    url(r'^new-game/', Index.as_view(), name="create-game"),
]
