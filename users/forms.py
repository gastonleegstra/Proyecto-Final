from django.forms import ModelForm
from users.models import User_profile

class User_profile_Form(ModelForm):
    class Meta:
        model = User_profile
        fields = ['phone','nombre','apellido','correo','profile_image']