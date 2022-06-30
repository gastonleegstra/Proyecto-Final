from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _

class Envase(models.Model):
    # Envase:
    # Tipo: clase del envase
    # capacidad: volumen del envase
    # medida: unidad de medida
    # activo: activo o no

    class Tipo(models.TextChoices):
        botella ='Botella', _('Botella')
        lata = 'Lata', _('Lata')   
    tipo = models.CharField(max_length=7,choices=Tipo.choices,null=True,blank=True)
    volumen = models.IntegerField(null=True,blank=True)
    class Medidas(models.TextChoices):
        lts='lts', _('lts')
        ml = 'ml', _('ml')
    medida = models.CharField(max_length=3,choices=Medidas.choices,null=True,blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo + ' '+ str(self.volumen)+ ' ' + self.medida

class Cerveza(models.Model):
    # Cerveza:
    # nombre: nombre de la cerveza
    # abv: cantidad de alcohol
    # ibu: armargor
    # precio: valor de venta
    # brew: tipo de levadura
    # color: color
    # envase: envase del producto
    # activo: activo o no

    nombre = models.CharField(max_length=50, null=True,blank=True)
    descripcion = models.TextField(max_length=500,null=True,blank=True)
    abv = models.IntegerField(null=True,blank=True)
    ibu = models.FloatField(null=True,blank=True)
    precio = models.FloatField(null=True,blank=True)
    class Tipo (models.TextChoices):
        ale = 'Ale', _('Ale')
        lager = 'Lager', _('Lager')
    class Color(models.TextChoices):
        golden = 'Golden', _('Golden')
        red = 'Red', _('Red')
        black = 'Black', _('Black')   
    tipo =models.CharField(max_length=5,choices=Tipo.choices, null=True,blank=True)
    brew = models.ForeignKey('Brew',on_delete=models.PROTECT,null=True,related_name='brews')
    color = models.CharField(max_length=6,choices=Color.choices, null=True,blank=True)
    envase = models.ForeignKey('Envase', on_delete=models.PROTECT,null=True,related_name='envases')
    categoria = models.ForeignKey('Categoria',on_delete=models.PROTECT,null=True,related_name='categorias')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Categoria (models.Model):
    categoria = models.CharField(max_length=50,null=True,blank=True)
    descripcion = models.TextField(max_length=150,null=True,blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.categoria

class Brew(models.Model):
    elaborador = models.CharField(max_length=30,null=True,blank=True)
    descripcion = models.TextField(max_length=150,null=True,blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.elaborador




