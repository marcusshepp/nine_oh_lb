from django.views.generic import TemplateView

from nine_oh_lb.settings import CHAMPION_STRINGS


class Index(TemplateView):

	template_name = "match/base_site.html"

class CreateGame(TemplateView):

	template_name = "match/game_form.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		context['champ_names'] = CHAMPION_STRINGS
		return context