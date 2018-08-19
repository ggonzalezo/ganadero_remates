from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from collections import OrderedDict
from .models import *
from .utils import *
from .forms import *
from datetime import datetime, timedelta
import simplejson as json
from itertools import filterfalse
from django import db
import heapq

def index(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.cleaned_data['animal']
            ciudad = form.cleaned_data['ciudad']
            feria = form.cleaned_data['feria']
            result_json = estadistica(request, ciudad, feria, animal)
            return HttpResponse(result_json, content_type='application/json')
    else:
        form = AnimalForm()

    return render(request, 'index.html', {'form': form})


def estadistica(request,ciudad, feria, animal):

    result = estadistica_basic(request, ciudad, feria, animal)

    result = json.dumps(result)

    return HttpResponse(result, content_type="application/json")
