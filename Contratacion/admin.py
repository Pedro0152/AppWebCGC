from django.contrib import admin
from .models import Contrato, Etapa, TrabajadorEtapa
from Entrada_de_datos.models import Cliente, Trabajador
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.

#class TrabajadorEtapa_Inline(admin.TabularInline):
#   model = TrabajadorEtapa
#  extra = 1

class EtapaInContrato_Inline(admin.TabularInline):
    model = Etapa

class ContratoAdmin(admin.ModelAdmin):
    #autocomplete_fields = ('nombre_de_cliente',)
    readonly_fields = ('created_Contrato', 'updated_Contrato')
    #list_display = ('numero_de_contrato','nombre_de_cliente', 'telefono') 
    list_display = ('numero_de_contrato','cliente','updated_Contrato')
    raw_id_fields = ['cliente']
    search_fields = ('numero_de_contrato', 'cliente')
    date_hierarchy = 'created_Contrato'
    inlines = [EtapaInContrato_Inline]
    #inlines= [TrabajadorEtapa_Inline]
    
    

admin.site.register(Contrato, ContratoAdmin)


