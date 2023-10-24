from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nombre

class TIPO_CHOICES(models.IntegerChoices):
    suspencion1 = 0, _('Suspencion de actividades')
    suspencion2 = 1, _('Suspencion de clases')
    informacion = 2, _('Informacion')
TIPO_CHOICES = models.IntegerField(choices=TIPO_CHOICES.choices)

class Comunicado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=200)
    tipo = TIPO_CHOICES
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.titulo