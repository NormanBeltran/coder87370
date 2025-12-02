from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - Comision {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model): 
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - Entregado: {self.entregado}"                