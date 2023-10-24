from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    title = "Inicio"
    objetos = Comunicado.objects.all()
    entidades = Entidad.objects.all()

    data = {
        "title": title,
        "objetos_guardados":objetos,
        "total_entidades":entidades
    }
    return render(request,"miapp\index.html", data)
