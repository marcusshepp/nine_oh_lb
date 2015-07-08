from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import GameForm, ChampionForm
from .models import Game, Champion, MatchHistory


class MatchHistoryView(TemplateView):

	template_name = "champ_select/match_history.html"
	model = MatchHistory()

	def get_context_data(self, *args, **kwargs):
		context = super(MatchHistoryView, self).get_context_data(**kwargs)
		context["cspermin"] = self.model.timeline_cspermin_all()
		return context