from django.db import models
from django.contrib.auth.models import User

class Mesa(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo= models.CharField(max_length= 30)
    precio = models.IntegerField()

    def __str__(self):
        return f'nombre: {self.nombre} - material: {self.material} - tipo: {self.tipo} - precio: {self.precio}'


class Silla(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo = models.CharField(max_length= 30)
    precio = models.IntegerField()

    
    def __str__(self):
        return f'nombre: {self.nombre} - material: {self.material} - tipo: {self.tipo} - precio: {self.precio}'



class Sofa(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo = models.CharField(max_length= 30)
    precio = models.IntegerField()

    
    def __str__(self):
        return f'nombre: {self.nombre} - material: {self.material} - tipo: {self.tipo} - precio: {self.precio}'


class Usuario(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido= models.CharField(max_length= 30)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    
    def __str__(self):
        return f'nombre: {self.nombre} - apellido: {self.apellido} - email: {self.email} - telefono: {self.telefono}'



class Avatar(models.Model):
    #Vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
