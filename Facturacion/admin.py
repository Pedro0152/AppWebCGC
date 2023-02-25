from django.contrib import admin

from Facturacion.models import Factura

# Register your models here.

class FacturaAdmin(admin.ModelAdmin):
      list_display = ('codigo','numero_de_factura','numero_de_contrato', 'numero_de_etapa','created')
      search_fields = ('codigo', 'numero_de_factura', 'numero_de_contrato')
      date_hierarchy = 'created'
      view_on_site = False

admin.site.register(Factura,FacturaAdmin)