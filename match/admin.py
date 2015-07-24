from django.contrib import admin

from .models import QuickGame, FavoriteChampion


class GamesInline(admin.TabularInline):

    model = FavoriteChampion.games.through


@admin.register(QuickGame)
class GameAdmin(admin.ModelAdmin):

    list_display = (
    	'__unicode__',
	)


@admin.register(FavoriteChampion)
class GameAdmin(admin.ModelAdmin):

    list_display = (
    	'__unicode__',
	)