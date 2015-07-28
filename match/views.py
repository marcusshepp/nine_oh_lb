from django.shortcuts import redirect, render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, View
from django.views.generic.list import MultipleObjectMixin as MOM
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from nine_oh_lb.settings import CHAMPION_STRINGS
from .models import QuickGame


class Index(TemplateView):

	template_name = "match/index.html"

	def get_unique_names(self):
		games = QuickGame.objects.all()
		x = [ i.user_played for i in games ]
		x = [ i for i in x if i != u"" ]
		return set(x)

		
class Common(TemplateView):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Common, self).dispatch(*args, **kwargs)


class CreateGame(Common):

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
			'user': request.user,
			'enemy_laner': request.POST['enemy_laner'],
			'user_played': request.POST['user_played'],
			'enemy_jungler': request.POST[
				'enemy_jungler'],
			'note': request.POST[
				'notes'],
			}
		QuickGame.objects.create(**obj_data)
		return redirect("/match/games/")


class AvailableGames(Common):
	""" Gamesr Inside Brain. """

	template_name = "match/games.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		games = QuickGame.objects.all().filter(user=self.request.user)
		paginator = Paginator(games, 4)
		page = self.request.GET.get("page")
		try:
			games = paginator.page(page)
		except PageNotAnInteger:
			games = paginator.page(1)
		except EmptyPage:
			games = paginator.page(paginator.num_pages)
		if len(games) > 0:
			context["games"] = games
		else:
			context["no_games"] = "Brain is empty of Games."
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


class ChampionDetail(Common):

	template_name = "match/champion_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		return context

	def post(self, request, *args, **kwargs):
		context = {}
		return context





