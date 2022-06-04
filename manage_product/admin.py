from django.contrib import admin
from manage_product.models import Capacidad, Cerveza,Envase, Precio

# Register your models here.
admin.site.register(Cerveza)
admin.site.register(Precio)
admin.site.register(Capacidad)
admin.site.register(Envase)