"""match URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
]
