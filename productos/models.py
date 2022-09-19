from django.db import models

# Create your models here.


class mesa(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo= models.CharField(max_length= 30)
    precio = models.IntegerField()


class silla(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo = models.CharField(max_length= 30)
    precio = models.IntegerField()


class sofa(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo = models.CharField(max_length= 30)
    precio = models.IntegerField()

class usuario(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido= models.CharField(max_length= 30)
    email = models.EmailField()
    telefono = models.IntegerField()
    