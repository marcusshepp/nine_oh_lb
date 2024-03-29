"""nine_oh_lb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin

from match import urls as match_urls
from registration import urls as user_urls
from charts import urls as api_urls


urlpatterns = [
	url(r'^$', RedirectView.as_view(url="match/", permanent=False)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^match/', include(match_urls)),
    url(r'^user/', include(user_urls)),
    url(r'^charts/', include(api_urls)),
]
