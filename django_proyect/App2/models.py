from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField(default=True)
    url_image = models.CharField(max_length=200, default="img/no-image.png")
    
    def __str__(self):
        return f"{self.nombre}"
    
    