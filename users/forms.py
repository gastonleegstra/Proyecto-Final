from dataclasses import field, fields
from socket import fromshare
from unicodedata import name
from django.forms import ModelForm
from users.models import User_profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User




class User_profile_Form(ModelForm):
    class Meta:
        model = User_profile
        fields = ['phone','nombre','apellido','correo','profile_image']



class User_registrarion_form(UserCreationForm):
    email = forms.CharField()
    password1: forms.CharField(label= 'contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label= 'Repita Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        help_texts = {k:'' for k in fields}