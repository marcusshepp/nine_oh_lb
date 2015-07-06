from django.views import generic as G
from django.shortcuts import render

from .forms import GameForm, ChampionForm
from .models import Game, Champion


class GameView(G.View):

	model = Game
	form_class = GameForm
	template_create = 'champ_select/item_create.html'
	template_list = 'champ_select/item_view.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class
		games = self.model.objects.all()
		template_data = {
			'form': form,
			'objects': games,
		}
		return render(request, self.template_create, template_data)

	def post(request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
		return render(request, self.template_list)


class ChampionView(G.View):

	model = Champion
	form_class = ChampionForm
	template_create = 'champ_select/item_create.html'
	template_list = 'champ_select/item_view.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class
		champions = self.model.objects.all()
		# games_played = 
		template_data = {
			'form': form,
			'objects': champions,
		}
		return render(request, self.template_list, template_data)

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()

		template_data = {
			'form': form,
			'objects': champions,
		}

		return render(request, self.template_create, template_data)

	def get_games_played(self, champion):
		""" Returns the number of games played for a champion. """
		return len(champion.games.objects.all())


