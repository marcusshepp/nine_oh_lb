from django.contrib import admin

from .models import Game, Champion


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_played'
    list_display = (
        '__unicode__',
    	'lane',
    	'cs',
    	'date_played',
	)

@admin.register(Champion)
class GameAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = (
    	'name',
        # 'get_average_cs',
	)
    fields = ['name']

