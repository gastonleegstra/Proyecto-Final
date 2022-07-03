from django.contrib import admin
from manage_product.models import Categoria, Cerveza,Envase, Brew

# Register your models here.
@admin.register(Cerveza)
class CervezaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'tipo', 'brew','color','envase','categoria','activo']

admin.site.register(Categoria)
admin.site.register(Brew)
admin.site.register(Envase)