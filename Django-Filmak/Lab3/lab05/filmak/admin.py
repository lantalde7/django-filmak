from filmak.models import Filma
from filmak.models import Bozkatzailea
from django.contrib import admin

class FilmaAdmin(admin.ModelAdmin):
	fieldsets=[
		('Izenburua',{'fields':['izenburua']}),
		('Zuzendaria',{'fields':['zuzendaria']}),
		('Urtea',{'fields':['urtea']}),
		('Generoa',{'fields':['generoa']}),
		('Sinopsia',{'fields':['sinopsia'],'classes':['collapse']}),
		('Bozkak',{'fields':['bozkak']}),
	]

admin.site.register(Filma,FilmaAdmin)
admin.site.register(Bozkatzailea)