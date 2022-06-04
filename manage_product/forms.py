from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from manage_product.models import Capacidad, Cerveza, Envase, Precio

class Capacidad_Form(ModelForm):
    class Meta:
        model = Capacidad
        fields = '__all__'

class Precio_Form(ModelForm):
    class Meta:
        model = Precio
        fields = '__all__'

class Envase_Form(ModelForm):
    class Meta:
        model = Envase
        fields = '__all__'

class Cerveza_Form(ModelForm):
    class Meta:
        model = Cerveza
        fields = '__all__'