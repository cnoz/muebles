from django import forms


class form_mesas(forms.Form):
    nombre = forms.CharField(max_length= 30)
    material = forms.CharField(max_length= 30)
    tipo = forms.CharField(max_length= 30)
    precio = forms.IntegerField()

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

class form_usuario(forms.Forml):
    nombre = forms.CharField(max_length= 30)
    apellido= forms.CharField(max_length= 30)
    email = forms.EmailField()
    telefono = forms.IntegerField()