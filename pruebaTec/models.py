from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/')