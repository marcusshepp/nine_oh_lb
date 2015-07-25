from django.shortcuts import render_to_response

from django.views.generic import TemplateView

from nine_oh_lb.settings import CHAMPION_STRINGS
from .models import QuickGame


class Index(TemplateView):

	template_name = "match/base_site.html"


class CreateGame(TemplateView):

	template_name = "match/game_form.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		context['champ_names'] = CHAMPION_STRINGS
		return context

	def post(self, request, *args, **kwargs):
		obj_data = {
			'user_played': request.POST['user_played'],
			'enemy_laner': request.POST['enemy_laner'],
			'winner': request.POST['winner'],
			'enemy_jungler': request.POST['enemy_jungler'],
			'note': request.POST['notes'],
		}
		QuickGame.objects.get_or_create(**obj_data)
		return render_to_response("match/games.html")


class GameView(TemplateView):

	template_name = "match/games.html"


