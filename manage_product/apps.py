from django.apps import AppConfig


class ManageProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manage_product'
#Coloco pseudonimo como se vera en el panel de administracion de Django
    verbose_name = "Gestion Productos - Cerveza"
