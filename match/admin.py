from django.contrib import admin

from .models import Match

class MatchAdmin(admin.ModelAdmin):

	model = Match


admin.site.register(Match, MatchAdmin)