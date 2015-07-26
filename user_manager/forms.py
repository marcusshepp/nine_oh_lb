from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class CustomUserCreationForm(UserCreationForm):
	username = forms.CharField(
		max_length=30,
		validators=[
			validators.RegexValidator(
			r'^[\w.@+-]+$',
			('Enter a valid username. This value may contain only '
			'letters, numbers ' 'and @/./+/-/_ characters.')
			),
		],
	error_messages={
	'unique': ("A user with that username already exists."),})
	password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput)