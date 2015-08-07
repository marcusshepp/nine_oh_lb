from django.contrib import admin

from .models import Game, FavoriteChampion


class GamesInline(admin.TabularInline):

    model = FavoriteChampion.games.through


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    list_display = (
    	'__unicode__',
	)


@admin.register(FavoriteChampion)
class GameAdmin(admin.ModelAdmin):

    list_display = (
    	'__unicode__',
	)