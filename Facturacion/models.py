from tkinter import CASCADE
from django.db import models
from Entrada_de_datos.models import Cliente
from Contratacion.models import Contrato,Etapa

# Create your models here.

class Factura(models.Model):
    codigo = models.PositiveSmallIntegerField('código')
    numero_de_factura = models.CharField('número de factura',max_length=20)
    numero_de_contrato = models.ForeignKey(Contrato,on_delete= models.CASCADE , null=False, blank= False)
    numero_de_etapa = models.OneToOneField(Etapa,on_delete = models.CASCADE, null = False, blank = False)
    factura = models.ImageField(upload_to = 'facturas')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'factura'
        verbose_name_plural = 'facturas'

    def __str__(self):
        return self.numero_de_factura

