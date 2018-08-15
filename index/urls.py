from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<slug:ciudad>/<slug:feria>/<slug:animal>',
		views.estadistica,
		name='estadistica'
	)
]