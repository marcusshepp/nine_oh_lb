from django.conf.urls import include, url

from .views import Register

urlpatterns = [
	url(r'^login/', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name="logout"),
    url(r'^register/', Register.as_view(), name="register"),
]
