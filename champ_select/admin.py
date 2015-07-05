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
class ChampionAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'date_created'
    fields = ['name']
    list_display = (
    	'name',
        'number_of_games',
        'average_cs'
	)

    def get_average_cs(self, **kwargs):
        """
        Returns average creepscore(cs).
        """
        total_cs = 0
        champ = Champion.objects.get()
        games = champ.games.all()
        for g in games:
            total_cs += g.cs
        value = total_cs / len(games)
        return value

