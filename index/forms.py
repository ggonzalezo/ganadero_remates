from django import forms

ANIMAL_CHOICES = (
	('Caballos', 'caballo'),
	('Cerdos', 'cerdo'),
	('Lanares', 'lanares'),
	('Novillos Engorda', 'novilloengorda'),
	('Novillos Gordos', 'novillogordo'),
	('Terneras', 'ternera'),
	('Terneros', 'ternero'),
	('Toros', 'toro'),
	('Vacas Engorda', 'vacaengorda'),
	('Vacas Gordas', 'vacagorda'),
	('Vaquillas Engorda', 'vaquillaengorda'),
	('Vaquillas Gordas', 'vaquillagorda'),
)

class AnimalForm(forms.Form):

	animal = forms.CharField(
		label='Animal', 
		max_length=100
	)
	ciudad = forms.CharField(
		label='Ciudad',
		max_length=100
	)
	feria = forms.CharField(
		label='Feria',
		max_length=100
	)