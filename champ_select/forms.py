from django import forms

from .models import Game, Champion


class GameForm(forms.ModelForm):
	
	class Meta:
		model = Game
		fields = [
			'champion',
			'enemy_laner',
			'lane',
			'win',
			'cs',
			'first_blood',
		]


class ChampionForm(forms.ModelForm):

	class Meta:
		model = Champion
		fields = [
			'name',
		]