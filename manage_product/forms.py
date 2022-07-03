from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from manage_product.models import Envase, Cerveza, Categoria, Brew

class Envase_Form(ModelForm):
    class Meta:
        model = Envase
        fields = '__all__'

class Cerveza_Form(ModelForm):
    class Meta:
        model = Cerveza
        fields = '__all__'

class Categoria_Form(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class Brew_Form(ModelForm):
    class Meta:
        model = Brew
        fields = '__all__'