from django.contrib import admin
from .models import Solicitud, Lugar
from Entrada_de_datos.models import Cliente, Trabajador
from admin_auto_filters.filters import AutocompleteFilter
from django.urls import path

# Register your models here.

class SolicitudAdmin(admin.ModelAdmin):
      autocomplete_fields = ('cliente', 'ejecuta' )
      readonly_fields = ('created', 'updated')
      list_display = ('fecha','proyecto', 'cliente', 'complejidad', 'valor') 
      search_fields = ('proyecto', 'cliente')
      date_hierarchy = 'updated'
      change_list_template = 'admin/Negociacion/solicitud_change_list.html'
      view_on_site = False
  
admin.site.register(Solicitud,SolicitudAdmin)
admin.site.register(Lugar)