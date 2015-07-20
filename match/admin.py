from django.contrib import admin

from .models import QuickGame


@admin.register(QuickGame)
class HubAdmin(admin.ModelAdmin):
    list_display = (
    	'user_played',
    	'enemy_laner',
    	'winner',
	)