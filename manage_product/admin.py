from django.contrib import admin
from manage_product.models import Categoria, Cerveza,Envase, Brew

# Register your models here.
admin.site.register(Cerveza)
admin.site.register(Categoria)
admin.site.register(Brew)
admin.site.register(Envase)