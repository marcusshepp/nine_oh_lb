from django.conf.urls import include, url
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from .forms import CustomUserCreationForm


urlpatterns = [
	url(r'^login/', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name="logout"),
    url(r'^register/', FormView.as_view(
    		form_class = CustomUserCreationForm,
    		success_url = reverse_lazy("games"),
    		template_name = "registration/register.html"
    	), name="register"),
]
