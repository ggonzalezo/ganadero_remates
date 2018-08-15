from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from .models import *
from datetime import datetime, timedelta
import simplejson as json
from itertools import filterfalse
from django import db
import heapq

def get_cities_universe():

	cities = Ciudades.objects.all()

	return cities

def get_ferias_universe():

	ferias = Ferias.objects.all()

	return ferias

def get_animal_universe(animal):
	if animal == 'caballo':
		animal = Caballos.objects.all()
	elif animal == 'cerdo':
		animal = Cerdos.objects.all()
	elif animal == 'lanares':
		animal = Lanares.objects.all()
	elif animal == 'novilloengorda':
		animal = NovillosEngorda.objects.all()
	elif animal == 'novillogordo':
		animal = NovillosGordo.objects.all()
	elif animal == 'ternera':
		animal = Terneras.objects.all()
	elif animal == 'ternero':
		animal = Terneros.objects.all()
	elif animal == 'toro':
		animal = Toros.objects.all()
	elif animal == 'vacaengorda':
		animal = VacasEngorda.objects.all()
	elif animal == 'vacagorda':
		animal = VacasGorda.objects.all()
	elif animal == 'vaquillaengorda':
		animal = VaquillasEngorda.objects.all()
	else:
		animal = VaquillasGorda.objects.all()

	return animal

def estadistica_basic(request, ciudad, feria, animal):

	cattle = animal
	company = feria
	city = ciudad

	caballos_universe = get_animal_universe(cattle)

	caballos_universe = caballos_universe.only(
			'fecha',
			'precio',
			'ciudad_feria'
			).order_by(
			'fecha'
			).select_related(
			'ciudad_feria'
			)

	if city:
		caballos_universe = caballos_universe.filter(
			ciudad_feria__ciudad=city,
			)

	if company:
		caballos_universe = caballos_universe.filter(
			ciudad_feria__ferias__feria=company
			)

	result = OrderedDict()

	for caballo in caballos_universe:
		
		date = caballo.fecha
		price = caballo.precio
		year = date.year
		month = date.month
		day = date.day
		ciudad = caballo.ciudad_feria.ciudad
		feria = caballo.ciudad_feria.ferias.feria

		if year not in result:
			result[year] = {}
		if month not in result[year]:
			result[year][month] = {
				'precio': []
			}
		result[year][month]['precio'].append([price, date.strftime('%m/%d'), ciudad, feria, cattle])
		result[year][month]['precio'].sort(reverse=True)

	return result
