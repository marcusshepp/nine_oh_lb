from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from match.models import (
	DetailedGame,
)

class CView(View):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(CView, self).dispatch(*args, **kwargs)


class APIKills(CView):

	def get(self, request, *args, **kwargs):
		dg = DetailedGame.objects.filter(user=request.user)
		games = {}
		for i in xrange(10):
			games[i] = dg[i].kill
		return JsonResponse(games)


class APICSPerMin(CView):

	def get(self, request, *args, **kwargs):
		dg = DetailedGame.objects.filter(user=request.user)
		games = {}
		for i in xrange(10):
			games[i] = [float(x) for x in dg[i].cs_per_min.split(",")]
		return JsonResponse(games)


class APIFullGame(CView):

	def get(self, request, *args, **kwargs):
		dg = DetailedGame.objects.filter(user=request.user).values()[0]
		return JsonResponse(dg)


class APIChampionDMG(CView):

	def get(self, request, *args, **kwargs):
		dg = DetailedGame.objects.filter(
			user=request.user, user_played__icontains=u"jinx").values()
		json_d = [x for x in dg]
		return JsonResponse(json_d, safe=False)


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
		return JsonResponse(json_d, safe=False)
