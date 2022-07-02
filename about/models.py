from django.db import models

# Create your models here.

class Developer(models.Model):
    nombre = models.CharField(max_length=150,null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to = 'developers', blank=True, null=True)

    def __str__(self):
        return self.nombre
