from django.contrib import admin
from estiamflixx.models import Serie


# Register your models here.

class SerieAdmin(admin.ModelAdmin):
    list_display=('id','titre','description','realisateur','annee_de_sortie','nbre_episodes')

admin.site.register(Serie,SerieAdmin)
