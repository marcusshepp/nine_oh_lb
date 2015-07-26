from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm


class Register(FormView):

	form_class = CustomUserCreationForm
	success_url = reverse_lazy("games")
	template_name = "registration/register.html"

	def form_valid(self, form):
		user = {
			"username": form.instance.username,
			"password": form.instance.username,
		}
		user_auth = authenticate(**user)
		user = User.objects.create(**user)
		if user is not None:
			if user.is_active:
				login(user)
				return reverse_lazy("games")