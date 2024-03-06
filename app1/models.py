from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    imagen = models.ImageField(upload_to='cursos/',  null=True, blank=True)
    detalle = models.CharField(max_length=500,)
    costo = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} | Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} | Profesion: {self.profesion}"
    
