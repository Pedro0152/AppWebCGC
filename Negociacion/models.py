#from concurrent.futures.process import _chain_from_iterable_of_lists
from asyncio.windows_events import NULL
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from Entrada_de_datos.models import Cargo, Cliente, Trabajador, Categoria_cientifica, Categoria_docente

# Create your models here.
class Lugar(models.Model):
    lugar = models.CharField(max_length= 100)
    class Meta:
        verbose_name = 'lugar'
        verbose_name_plural = 'lugares'

    def __str__(self):
        return self.lugar 

class Solicitud(models.Model):
    fecha = models.DateField()
    de = models.ForeignKey(Lugar, on_delete=models.CASCADE, null = False, blank= False, default= 'Departamento Filial Oriental (Santiago de Cuba)')
    propuestas = [
      ('1','Suplemento'),  ('2','Contrato')
    ]
    propuesta = models.CharField(max_length= 30, choices=propuestas,default='1')
    tipos = [
      ('1','Servicio'),  ('2','Proyecto')
    ]
    tipo = models.CharField(max_length= 30, choices=tipos,default='1')
    complejidades = [
      ('1','alta'),  ('2','media'),
      ('3','baja')
    ]
    complejidad = models.CharField(max_length= 30, choices=complejidades,default='1')
    proyecto = models.CharField(max_length=100, null= False, blank= False)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, max_length= 200, null= False , blank=False )
    tipos_de_Clientes = [
      ('1','Encargo estatal'),  ('2','MINCIN'),
      ('3','Tercero')
    ]
    tipos_de_Clientes = models.CharField(max_length= 30, choices=tipos_de_Clientes,default='1')
    valor =models.PositiveIntegerField(null = False, blank= False)
    duracion = models.PositiveSmallIntegerField("Duración(meses)",null = False, blank= False)
    ejecuta = models.ForeignKey(Trabajador,related_name="%(app_label)s_%(class)s_ejecutor", on_delete=models.CASCADE, null = False, blank= False)
    #cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null = True, blank= True)
    colaborador = models.ManyToManyField(Trabajador)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.proyecto    

    class Meta:
        verbose_name = 'solicitud'
        verbose_name_plural = 'solicitudes'
