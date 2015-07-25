from django.shortcuts import render_to_response
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import MultipleObjectMixin as MOM

from nine_oh_lb.settings import CHAMPION_STRINGS
from .models import QuickGame


class Index(TemplateView):

	template_name = "match/base_site.html"

	def get_unique_names(self):
		games = QuickGame.objects.all()
		x = [ i.user_played for i in games ]
		x = [ i for i in x if i != u"" ]
		return set(x)


class CreateGame(Index):

	template_name = "match/game_form.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		context['champ_names'] = CHAMPION_STRINGS
		return context

	def post(self, request, *args, **kwargs):
		obj_data = {}
		if "winner" in request.POST:
			obj_data["winner"] = True
		else: obj_data["winner"] = False
		obj_data = {
			'enemy_laner': request.POST['enemy_laner'],
			'user_played': request.POST['user_played'],
			'enemy_jungler': request.POST[
				'enemy_jungler'],
			'note': request.POST[
				'notes'],
			}
		QuickGame.objects.get_or_create(**obj_data)
		return render_to_response(
			"match/games.html",
			)


class AvailableGames(Index, MOM):

	template_name = "match/games.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		games = QuickGame.objects.all()
		context['games'] = [x for x in games]
		# context['names'] = games
		return context

	def post(self, request, *args, **kwargs):
		context = {}
		champs = QuickGame.objects.filter(
			name=request.POST['name'],
			)
		context['champs_after_post'] = champs
		return context


class GameDetail(DetailView):

	model = QuickGame
	template_name = "match/game_detail.html"


class ChampionDetail(Index):

	template_name = "match/champion_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		return context

	def post(self, request, *args, **kwargs):
		context = {}
		return context





