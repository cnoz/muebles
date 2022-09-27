from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_mesas(forms.Form):
    nombre = forms.CharField(max_length= 30)
    material = forms.CharField(max_length= 30)
    tipo = forms.CharField(max_length= 30)
    precio = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label='Repetir Contraseña', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username','email', 'password1', 'password2']
        help_texts = {k: "" for k in fields} 




class form_sillas(forms.Form):
    nombre = forms.CharField(max_length= 30)
    material = forms.CharField(max_length= 30)
    tipo = forms.CharField(max_length= 30)
    precio = forms.IntegerField()

class form_sillones(forms.Form):
    nombre = forms.CharField(max_length= 30)
    material = forms.CharField(max_length= 30)
    tipo = forms.CharField(max_length= 30)
    precio = forms.IntegerField()

class form_usuario(forms.Form):
    nombre = forms.CharField(max_length= 30)
    apellido= forms.CharField(max_length= 30)
    email = forms.EmailField()
    telefono = forms.IntegerField()