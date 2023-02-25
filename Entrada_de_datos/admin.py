from django.contrib import admin
from .models import *

admin.site.site_header = 'Sistema CGC'
admin.site.index_title = 'Panel de Control'
#admin.site.site_title = 'Titulo en la pestaña del navegador'


# Register your models here.

class TrabajadorAdmin(admin.ModelAdmin):
      list_display = ('nombre','ci','Categoria_cientifica','Categoria_docente', 'created') 
      search_fields = ('nombre', 'ci',)
      #readonly_fields = ('created', 'updated')
      date_hierarchy = 'created'
      view_on_site = False

class ClienteAdmin(admin.ModelAdmin):
      list_display = ('nombre_cliente','telefono','nit', 'codigoREEUP','email')
      search_fields = ('nombre_cliente', 'nit', 'codigoREEUP')
      date_hierarchy = 'created'
      view_on_site = False

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Categoria_cientifica)
admin.site.register(Categoria_docente)
admin.site.register(Cargo)
