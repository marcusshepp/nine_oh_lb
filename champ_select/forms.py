from django import forms

from .models import Game, Champion


class GameForm(forms.ModelForm):
	
	class Meta:
		model = Game
		fields = [
			'champion',
			'lane',
			'win',
			'cs',
			'first_blood',
			'confidence_level'
		]


class ChampionForm(forms.ModelForm):

	class Meta:
		model = Champion
		fields = [
			'name',
		]