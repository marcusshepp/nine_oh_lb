import json

from django.shortcuts import redirect, render_to_response, render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, View
from django.views.generic.list import MultipleObjectMixin as MOM
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from nine_oh_lb.settings import CHAMPION_STRINGS
from pyblanc.pyblanc import LeagueStat
from .models import (
	Game,
)


class Index(TemplateView):

	template_name = "match/index.html"

	def get_unique_names(self):
		games = Game.objects.all()
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
			'direct_enemy': request.POST['direct_enemy'],
			'user_played': request.POST['user_played'],
			'what_you_did_well': request.POST[
				'what_you_did_well'],
			'could_have_done_better': request.POST[
				'could_have_done_better'],
			}
		Game.objects.create(**obj_data)
		return redirect("/match/games/")


class AvailableGames(Common):
	""" Games Inside Brain. """

	template_name = "match/games.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		games = Game.objects.all().filter(user=self.request.user)
		count = len(games)
		paginator = Paginator(games, 4)
		page = self.request.GET.get("page")
		try:
			games = paginator.page(page)
		except PageNotAnInteger:
			games = paginator.page(1)
		except EmptyPage:
			games = paginator.page(paginator.num_pages)
		if len(games) > 0:
			context["count"] = count
			context["games"] = games
		else:
			context["no_games"] = True
		return context

	def post(self, request, *args, **kwargs):
		context = {}
		games = Game.objects.filter(user=self.request.user)
		games = games.filter(user_played__istartswith=request.POST["c_search"])
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
			context["no_games"] = True
		context["user"] = request.user
		return render(request, "match/games.html", context)


class AvailableChamps(Common):
	""" Champs Inside Brain. """

	template_name = "match/champs.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		champs = Game.objects.all().filter(user=self.request.user)
		champs = [x.user_played for x in champs]
		champs = list(set(champs))
		paginator = Paginator(champs, 4)
		page = self.request.GET.get("page")
		try:
			champs = paginator.page(page)
		except PageNotAnInteger:
			champs = paginator.page(1)
		except EmptyPage:
			champs = paginator.page(paginator.num_pages)
		if len(champs) > 0:
			context["champs"] = champs
		else:
			context["no_champs"] = True
		return context

	def post(self, request, *args, **kwargs):
		context = {}
		champs = Game.objects.filter(user=self.request.user)
		champs = champs.filter(user_played__istartswith=request.POST["c_search"])
		paginator = Paginator(champs, 4)
		page = self.request.GET.get("page")
		try:
			champs = paginator.page(page)
		except PageNotAnInteger:
			champs = paginator.page(1)
		except EmptyPage:
			champs = paginator.page(paginator.num_pages)
		if len(champs) > 0:
			context["champs"] = champs
		else:
			context["no_champs"] = True
		context["user"] = request.user
		return render(request, "match/champs.html", context)


class GameDetail(DetailView):

	model = Game
	template_name = "match/game_detail.html"


class ChampionDetail(Common):

	template_name = "match/champion_detail.html"


class CreateGeniusGameData(View):

	def convert_permin(self, data):
			x = ",".join(str(i) for k, i in data.items()) # thanks Kevin Daum
			return x

	def get(self, request, *args, **kwargs):
		user_data = {}
		user_data['summoner'] = request.user.get_username()
		ls = LeagueStat(**user_data)
		user_played = ls.all_champions()
		wsls = ls.winsandloses()
		total_cs = ls.all_minions_killed()
		cs_per_min = ls.cs_per_min()
		xp_per_min = ls.xp_per_min()
		dmg_to_champions = ls.damage_dealt_to_champions()
		fb = ls.first_blood()
		ge = ls.gold_earned()
		ks = ls.longest_killing_spree()
		mk = ls.largest_multikill()
		minions = ls.all_minions_killed()
		wp = ls.wards_placed()
		kills = ls.kills()
		deaths = ls.deaths()
		assists = ls.assists()
		tk = ls.towers_killed()
		g_data = {}
		for i in xrange(10):
			g_data['user'] = request.user
			g_data['user_played'] = user_played[i]
			g_data['winner'] = wsls[i]
			g_data['cs'] = total_cs[i]
			g_data['cs_per_min'] = self.convert_permin(cs_per_min[i])
			g_data['xp_per_minute'] = self.convert_permin(xp_per_min[i])
			g_data['damage_done'] = dmg_to_champions[i] #!!!
			g_data['first_blood'] = fb[i]
			g_data['gold_earned'] = ge[i]
			g_data['killing_spree'] = ks[i]
			g_data['largest_multikill'] = mk[i]
			g_data['dmg_to_champions'] = dmg_to_champions[i]
			g_data['wards_placed'] = wp[i]
			g_data['kill'] = kills[i]
			g_data['death'] = deaths[i]
			g_data['assist'] = assists[i]
			g_data['tower'] = tk[i]
			Game.objects.get_or_create(**g_data)
		return redirect("/games")