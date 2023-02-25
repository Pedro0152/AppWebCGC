from ast import arg
from cgi import print_form
from csv import QUOTE_MINIMAL
from email.policy import default
from multiprocessing.connection import Client
from tokenize import blank_re
from webbrowser import get
from django.db import models
from Entrada_de_datos.models import Trabajador, Cliente
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

class Contrato(models.Model):
    numero_de_contrato = models.PositiveIntegerField('número de contrato', null= True, blank= True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null = False, blank= False)
    representante = models.CharField(max_length=200, null= False, blank= False)
    cargo = models.CharField(max_length=200, null= False, blank= False)
    resolucion = models.CharField (max_length=100, null=False, blank=False, default= '120 del 1 de marzo de 2021')
    contrato = models.FileField(upload_to = 'contratos')
    #anexo1 = models.FileField(upload_to = 'anexos')
    #anexo2 = models.FileField(upload_to = 'anexos')
    #en_ejecucion = models.CheckConstraint()
    colaboradores = models.ManyToManyField(Trabajador)
    created_Contrato = models.DateTimeField(auto_now_add = True)
    updated_Contrato = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.numero_de_contrato)

    class Meta:
        verbose_name = 'contrato'
        verbose_name_plural = 'contratos'

class Etapa(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete = models.CASCADE, null = False, blank = False)
    numero_de_etapa = models.AutoField(primary_key=True)
    cabecera = models.CharField(max_length=50, null = False, blank = False)
    descripcion = models.CharField(max_length=200,null=False, blank= False)
    duracion = models.PositiveSmallIntegerField('duracion(meses)')
    importe = models.PositiveIntegerField(null= True, blank= True, default=0.00 )
    #colaboradores = models.ManyToManyField(Trabajador,through= 'TrabajadorEtapa' )

    def __str__(self):
        return str(self.numero_de_etapa)

class TrabajadorEtapa(models.Model):
    trabajador = models.ForeignKey(Trabajador,on_delete= models.CASCADE, blank = False, null = False)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, blank = False, null = False)
    contrato = models.ForeignKey(Contrato,on_delete= models.CASCADE, blank = False, null = False)
    porcentaje = models.PositiveSmallIntegerField('%',blank = False, null = False,default =0 )



