from django.contrib import admin
from index.models import Ciudades, Ferias, Caballos, Cerdos, Lanares, NovillosEngorda, NovillosGordo, Terneras, Terneros, Toros, VaquillasEngorda, VaquillasGorda, VacasEngorda, VacasGorda

class CiudadesAdmin(admin.ModelAdmin):
	fields = (
		'ciudad',
		'ferias',
	)

class FeriasAdmin(admin.ModelAdmin):
	fields = (
		'feria',
	)

admin.site.register(Ciudades)
admin.site.register(Ferias)
admin.site.register(Caballos)
admin.site.register(Cerdos)
admin.site.register(Lanares)
admin.site.register(NovillosEngorda)
admin.site.register(NovillosGordo)
admin.site.register(Terneras)
admin.site.register(Terneros)
admin.site.register(Toros)
admin.site.register(VaquillasEngorda)
admin.site.register(VaquillasGorda)
admin.site.register(VacasEngorda)
admin.site.register(VacasGorda)
