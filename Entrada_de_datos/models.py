from unittest.util import _MAX_LENGTH
from django.db import models
from admin_auto_filters.filters import AutocompleteFilter
# Create your models here.

class Cliente(models.Model):
    nombre_cliente = models.CharField("nombre de cliente", max_length=200,null = False, blank= False)
    empresa_matriz = models.CharField ("subordinada a", max_length= 200, null=True, blank=True)
    direccion = models.CharField("dirección", max_length=200, null= False, blank=False)
    provincias = [
      ('1','Santiago de Cuba'),  ('9','Guantánamo'),
      ('2','Las Tunas'),  ('10','Holguín'),
      ('3','Granma'),  ('11','Camagüey'),
      ('4','Artemisa'),  ('12','Mayabeque'),
      ('5','Pinar del Río'),  ('13','La Habana'),
      ('6','Isla de la Juventud'),  ('14','Sanctis Spiritus'),
      ('7','Villa Clara'),  ('15','Cienfuegos'),
      ('8','Matanzas'),  ('16','Ciego de Ávila')
    ]
    provincia = models.CharField(max_length= 30, choices=provincias,default='1')
    municipio = models.CharField(max_length= 30, default= 'Santiago de Cuba')
    codigoREEUP = models.PositiveBigIntegerField(null = False, blank= False)
    nit = models.PositiveBigIntegerField(primary_key= True)  
    cuenta_bancaria = models.PositiveBigIntegerField()
    sucursal = models.PositiveSmallIntegerField()
    bancos = [
        ('1','BANDEC'),
        ('2','BPA')
        ]
    banco = models.CharField(max_length= 20, choices=bancos, default='1')    
    telefono = models.PositiveBigIntegerField()
    email = models.EmailField(null= True, blank= True)
    titular_de_cuenta_bancaria = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return str(self.nombre_cliente)
        


class Cargo(models.Model):
    nombre = models.CharField(max_length = 30)
    class Meta:
        verbose_name = 'cargo'
    def __str__(self):
        return self.nombre

class Categoria_docente(models.Model):
    nombre = models.CharField(max_length = 50)
    class Meta:
        verbose_name = 'categoría docente'
    def __str__(self):
        return self.nombre

class Categoria_cientifica(models.Model):
    nombre = models.CharField(max_length = 30)
    class Meta:
        verbose_name = 'categoría científica'
    def __str__(self):
        return self.nombre   

class Trabajador(models.Model):
    nombre = models.CharField(max_length=20,null = False, blank = False)
    ci = models.PositiveBigIntegerField()  
    telefono = models.PositiveBigIntegerField()
    direccion = models.CharField(max_length=50)
    Categoria_cientifica=models.ForeignKey(Categoria_cientifica, on_delete=models.CASCADE, null = False, blank= False)
    Categoria_docente=models.ForeignKey(Categoria_docente, on_delete=models.CASCADE, null = False, blank= False)
    cargo = models.ForeignKey(Cargo , on_delete=models.CASCADE, null = False, blank = False)
    #contratos_realizados-----aporte
    #aporte total------- #
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'trabajador'
        verbose_name_plural = 'trabajadores'

    def __str__(self):
        return self.nombre


