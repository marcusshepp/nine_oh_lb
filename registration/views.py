from django.shortcuts import render, redirect, render_to_response
from django.views.generic import View
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, UserLoginForm

class UserRegistrationView(FormView):

	form_class = UserRegistrationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('games')

	def form_valid(self, form):
		form.save()
		return super(UserRegistrationView, self).form_valid(form)


class Login(View):

	def get(self, request):
		form = UserLoginForm()
		return render(request, 'registration/login.html', {'form': form})

	def post(self, request):
		form = UserRegistrationForm(data=request.POST)
		if form.is_valid:
			user = authenticate(
				username=request.POST['summoner_name'], 
				password=request.POST['password']
				)
			if user is not None:
				if user.is_active:
					login(request, user)
					user.is_authenticated = True
					return redirect('games')
		form = UserLoginForm()
		message = 'User not authenticated'
		return render_to_response('registration/login.html', {"message": message, "form": form}, context_instance=RequestContext(request))