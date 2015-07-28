from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, UserLoginForm


class Register(FormView):

	form_class = CustomUserCreationForm
	success_url = reverse_lazy("games")
	template_name = "registration/register.html"

	def post(self, request):
		user = {
			"username": request.POST['username'],
			"password": request.POST['password1'],
		}
		user = User.objects.create_user(**user)
		user = authenticate()
		if user is not None:
			if user.is_active:
				login(request, user)
				return reverse_lazy("games")


class Login(FormView):

	form_class = UserLoginForm
	success_url = reverse_lazy("games")
	template_name = "registration/login.html"

	def post(self, request):
		user = {
			"username": request.POST['username'],
			"password": request.POST['password1'],
		}
		user = authenticate(user)
		if user is not None:
			if user.is_active:
				login(request, user)
				return reverse_lazy("games")