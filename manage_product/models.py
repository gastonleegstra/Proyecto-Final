from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _

class Capacidad(models.Model):
    #Capacidad:
    # volumen: capacidad del envase
    # medida: medida de medida litros o mililitros
    # activo: activo o no
    
    volumen = models.IntegerField(null=True,blank=True)
    class Medidas(models.TextChoices):
        lts='lts', _('lts')
        ml = 'ml', _('ml')
    medida = models.CharField(max_length=3,choices=Medidas.choices,null=True,blank=True) 
    activo = models.BooleanField(default=True)

class Precio(models.Model):
    # Price:
    # price: ej: 250
    # fecha_alta: fecha de alta del precio
    # activo: activo o no

    precio = models.FloatField(null=True,blank=True)
    fecha_alta = models.DateField(default=date.today())
    activo = models.BooleanField(default=True)

class Envase(models.Model):
    # Envase:
    # Tipo: clase del envase
    # capacidad: volumen del envase
    # activo: activo o no

    class Tipo(models.TextChoices):
        botella ='Botella', _('Botella')
        lata = 'Lata', _('Lata')   
    tipo = models.CharField(max_length=7,choices=Tipo.choices,null=True,blank=True)
    capacidad = models.OneToOneField(Capacidad,on_delete=models.CASCADE,primary_key=True)
    activo = models.BooleanField(default=True)

class Cerveza(models.Model):
    # Cerveza:
    # nombre: nombre de la cerveza
    # abv: cantidad de alcohol
    # ibu: armargor
    # brew: tipo de levadura
    # color: color
    # envase: envase del producto
    # activo: activo o no

    nombre = models.CharField(max_length=50, null=True,blank=True)
    descripcion = models.TextField(max_length=500,null=True,blank=True)
    abv = models.IntegerField(null=True,blank=True)
    ibu = models.FloatField(null=True,blank=True)
    precio = models.OneToOneField(Precio,on_delete=models.CASCADE,primary_key=True)
    class Brew (models.TextChoices):
        ale = 'Ale', _('Ale')
        lager = 'Lager', _('Lager')
    class Color(models.TextChoices):
        golden = 'Golden', _('Golden')
        red = 'Red', _('Red')
        black = 'Black', _('Black')   
    brew =models.CharField(max_length=5,choices=Brew.choices, null=True,blank=True)
    color = models.CharField(max_length=6,choices=Color.choices, null=True,blank=True)
    envase = models.ForeignKey(Envase, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)




