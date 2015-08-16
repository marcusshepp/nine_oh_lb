import operator
import collections

from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response, render

from match.models import (
	Game,
)

class CView(View):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(CView, self).dispatch(*args, **kwargs)


class Genius(CView):

	template_name = "charts/index.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)


class APIKills(CView):

	def get(self, request, *args, **kwargs):
		dg = Game.objects.filter(user=request.user)
		kills = [x.kill for x in dg]
		champs = [x.user_played for x in dg]
		games = {}
		games['champs'] = champs
		games['kills'] = kills
		return JsonResponse(games)


class APICSPerMin(CView):

	def get(self, request, *args, **kwargs):
		dg = Game.objects.filter(user=request.user)
		games = {}
		for i in xrange(10):
			games[i] = [float(x) for x in dg[i].cs_per_min.split(",")]
		return JsonResponse(games)


class APIFullGame(CView):

	def get(self, request, *args, **kwargs):
		dg = Game.objects.filter(user=request.user).values()[0]
		return JsonResponse(dg)


class APIChampionDMG(CView):

	def post(self, request, *args, **kwargs):
		dg = Game.objects.filter(
			user=request.user, user_played__icontains=u"{}".format(self.request.POST['c_search']))
		json_d = {}
		json_d['champions'] = [x.user_played for x in dg if x.dmg_to_champions]
		json_d['dmg'] = [x.dmg_to_champions for x in dg if x.dmg_to_champions]
		return JsonResponse(json_d)


class ChampionDMG(CView):

	template_name = "charts/champion_dmg.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)


class APIChampionGoldAll(CView):

	def get(self, request, *args, **kwargs):
		dg = Game.objects.filter(user=request.user)
		json_d = {}
		json_d['champions'] = [x.user_played for x in dg if x.dmg_to_champions]
		json_d['gold'] = [x.gold_earned for x in dg if x.gold_earned]
		return JsonResponse(json_d, safe=False)


class ChampionGoldAll(CView):

	template_name = "charts/compare_gold.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)


class ChampionGoldComparison(CView):
	
	template_name = "charts/champ_gold_comparison.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)


class APIChampionGoldComparison(CView):
	
	def post(self, request, *args, **kwargs):
		"""
		post data: champion1 champion2
		return damage for all games played for each champion. 
		maybe all damage added together for each champion?
		this would be good because then this view would only return 
		four values: name1 dmg1 name2 dmg2
		"""
		search_one = request.POST['c_search_one']
		search_two = request.POST['c_search_two']
		query_one = Game.objects.filter(user=request.user, user_played__istartswith=search_one)
		query_two = Game.objects.filter(user=request.user, user_played__istartswith=search_two)
		highest_one = query_one.order_by("gold_earned")[:1]
		highest_two = query_two.order_by("gold_earned")[:1]
		json_d = {}
		json_d['champ_one'] = [v.user_played for v in highest_one if v.gold_earned]
		json_d['champ_two'] = [v.user_played for v in highest_two if v.gold_earned]
		json_d['gold_one'] = [v.gold_earned for v in highest_one if v.gold_earned]
		json_d['gold_two'] = [v.gold_earned for v in highest_two if v.gold_earned]
		return JsonResponse(json_d)


class APIGamesPlayedTopFive(CView):

	def get(self, request, *args, **kwargs):
		"""
		return top 5 champions played 
		and the number of games played with those champs
		"""
		json_d = {}
		gs = Game.objects.filter(user=request.user)
		champs_user_played = [x.user_played for x in gs]
		for value in champs_user_played:
			if not value in json_d:
				json_d[value] = 1
			else: json_d[value] += 1
		sorted_json_d = collections.OrderedDict(sorted(json_d.items(), key=lambda t: t[0]))
		return_obj = {}
		return_obj["champions"] = [k for k, v in sorted_json_d.items()][:5]
		return_obj["games_played"] = [v for k, v in sorted_json_d.items()][:5]
		return JsonResponse(return_obj)


class TopFiveChampionsPlayed(CView):

	template_name = "charts/top_five_champs_played.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

