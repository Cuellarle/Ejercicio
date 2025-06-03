from django.db import models

#Creacion de modelos
class Menu(models.Model):
    
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)
    precio = models.IntegerField()
    tiempo = models.IntegerField(default = 10)
    
    def __str__(self):
        return self.nombre + ": " + self.descripcion + " $" + str(self.precio) 


class Logger(models.Model):
    turnos = [('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')]
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    turno = models.CharField(max_length = 1, choices = turnos)  
    hora_llegada = models.TimeField(help_text = "Ingrese la hora exacta")

    def __str__(self):
        return self.nombre + " " + self.apellido + " - " + self.turno

    
# Create your models here.

#Ejemplo de como influyen algunas configuraciones de 
class Persona(models.Model):
    apellidos = models.TextField(max_length=100)
    nombres = models.TextField(max_length=100)
    
    def __str__(self):
        return self.apellidos + " " + self.nombres 

