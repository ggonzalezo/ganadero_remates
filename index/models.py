from django.db import models

class Ciudades(models.Model):
	ciudad = models.CharField(max_length=200)
	ferias = models.ForeignKey(
		'Ferias',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return str(self.ciudad+', '+self.ferias.feria)

class Ferias(models.Model):
	feria = models.CharField(max_length=200)
	def __str__(self):
		return self.feria

class Caballos(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return 'Caballo'
	
class Cerdos(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Cerdo'

class Lanares(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Lanar'

class NovillosEngorda(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Novillo Engorda'

class NovillosGordo(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Novillo Gordo'

class Terneras(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Ternera'

class Terneros(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Ternero'

class Toros(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Toro'

class VaquillasEngorda(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Vaquilla Engorda'

class VaquillasGorda(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Vaquilla Gorda'

class VacasEngorda(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Vaca Engorda'

class VacasGorda(models.Model):
	fecha = models.DateField(
		auto_now=False,
		auto_now_add=False,
	)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	ciudad_feria = models.ForeignKey(
		'Ciudades',
		on_delete=models.CASCADE
	)
	def __str__(self):
		return 'Vaca Gorda'
