from django.db import models

# Create your models here.


class Mesa(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo= models.CharField(max_length= 30)
    precio = models.IntegerField()


class Silla(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo = models.CharField(max_length= 30)
    precio = models.IntegerField()


class Sofa(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo = models.CharField(max_length= 30)
    precio = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido= models.CharField(max_length= 30)
    email = models.EmailField()
    telefono = models.IntegerField()
    