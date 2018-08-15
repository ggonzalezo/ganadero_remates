from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from .models import *
from datetime import datetime, timedelta
import simplejson as json
from itertools import filterfalse
from django import db

def get_ciudadferia(city, feria):
	
	if '_' in city:
		city = city.replace('_', ' ')
		city = city.title()
		part = city.split(' ')
		rio_part = part[0]
		if 'Rio' in rio_part:
			rio_part = 'Río'
			city = rio_part+' '+part[1]
		elif 'Pto' in rio_part:
			rio_part = 'Puerto'
			city = rio_part+' '+part[1]
	elif city == 'calera':
		city = 'La Calera'
	elif city == 'curico':
		city = 'Curicó'
	else:
		city = city.title()
	
	if feria == 'calera_sa':
		feria = 'La Calera'
	elif feria == 'araucania':
		feria = 'Araucanía'
	elif feria == 'biobio':
		feria = 'Biobío'
	else:
		feria = feria.title()
	
	ciudades = Ciudades.objects.filter(
		ciudad=city,
		ferias__feria=feria
	)
	
	return ciudades[0]

def get_float(precio):
	
	count = 0
	palabra = []
	word = []
	first = True
	
	if precio == '':
		precio = 0
		return precio

	for n in precio:
		if n == '.':
			count += 1
		palabra.append(n)

	if count<2:
		return float(precio)

	for x in palabra:
		if x == '.':
			if first == True:
				continue
			first = False
		word.append(x)

	precio = ''.join(word)
	precio = float(precio)
	
	return precio

def index(request):

	with open(r'C:/Users/miguel/Documents/Ganadero2/ganadero/index/historico_ciudad_empresa_remate_(split;).json') as data:
		code = json.load(data)

	a = OrderedDict()
	
	for ciudad in code:
		for empresa in code[ciudad]:
			for animal in code[ciudad][empresa]:
				key = code[ciudad][empresa][animal]
				if isinstance(key, int):
					key = {'Data': '0,0;0,0'}
				key = key['Data'].split(';')
				for element in key:
					element = element.split(',')
					fecha, precio = element
					
					if animal not in a:
						a[animal] = {}
					
					if ciudad not in a[animal]:
						a[animal][ciudad] = {}
					
					if empresa not in a[animal][ciudad]:
						a[animal][ciudad][empresa] = {}
					
					if fecha not in a[animal][ciudad][empresa]:
						a[animal][ciudad][empresa][fecha] = 0
					
					a[animal][ciudad][empresa][fecha] = precio

	for animal in a:
		for ciudad in a[animal]:
			for empresa in a[animal][ciudad]:
				for fecha in a[animal][ciudad][empresa]:
					precio = a[animal][ciudad][empresa][fecha]
					precio = get_float(precio)
					if precio == '0':
						continue
					if fecha == '0':
						continue
					fecha = datetime.strptime(fecha, '%Y/%m/%d')
					ciudad_feria = get_ciudadferia(ciudad, empresa)
					print(animal, ciudad_feria,  precio, fecha)
					if animal == 'caballo':
						objeto = Caballos(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'cerdo':
						objeto = Cerdos(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'lanares':
						objeto = Lanares(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'novilloengorda':
						objeto = NovillosEngorda(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'novillogordo':
						objeto = NovillosGordo(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'ternera':
						objeto = Terneras(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'ternero':
						objeto = Terneros(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'toro':
						objeto = Toros(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'vacaengorda':
						objeto = VacasEngorda(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'vacagorda':
						objeto = VacasGorda(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'vaquillaengorda':
						objeto = VaquillasEngorda(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					elif animal == 'vaquillagorda':
						objeto = VaquillasGorda(
							fecha=fecha,
							precio=precio,
							cantidad=0,
							ciudad_feria=ciudad_feria,
						)
					# objeto.save()

	# db.connections.close_all()

	# Caballos.objects.all().delete()
	# Cerdos.objects.all().delete()
	# Lanares.objects.all().delete()
	# NovillosGordo.objects.all().delete()
	# NovillosEngorda.objects.all().delete()
	# Terneras.objects.all().delete()
	# Terneros.objects.all().delete()
	# Toros.objects.all().delete()
	# VaquillasEngorda.objects.all().delete()
	# VaquillasGorda.objects.all().delete()
	# VacasGorda.objects.all().delete()
	# VacasEngorda.objects.all().delete()

	print('Success!')
	
	# return HttpResponse(a, content_type='application/json')
	return HttpResponse('Full DB Integration - Try Nº1')
	# return HttpResponse('DB - Caballos')
	# return HttpResponse('Deleted')
	# return HttpResponse('Test - Good!')
	# return HttpResponse('Closed DB processes')