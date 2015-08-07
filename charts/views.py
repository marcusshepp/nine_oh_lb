import operator

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
		games = {}
		for i in xrange(10):
			games[i] = dg[i].kill
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
			user=request.user, user_played__icontains=u"{}".format(self.request.POST['c_search'])).values()
		json_d = {}
		for i in dg:
			if i["dmg_to_champions"]:
				json_d[i["user_played"]] = i["dmg_to_champions"]
		return JsonResponse(json_d)


class ChampionDMG(CView):

	template_name = "charts/champion_dmg.html"

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
		return JsonResponse(json_d, safe=False)


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
		sorted_json_d = sorted(json_d.items(), key=operator.itemgetter(1))[1:6]
		return JsonResponse(sorted_json_d, safe=False)


class TopFiveChampionsPlayed(CView):

	template_name = "charts/top_five_champs_played.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

