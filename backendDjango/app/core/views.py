from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from datetime import datetime
import json
from app.jurisprudencias.functions import obtener_jurisprudencia
from app.jurisprudencias.models import Jurisprudencia
from django.shortcuts import render
from app.concesionesmaritimas.models import Concesion
from app.concesionesmaritimas.function import obtener_informacion





def Jurisprudencia_view(request):
    # Obtener y guardar la jurisprudencia
    obtener_jurisprudencia()

    # Obtener los datos de la jurisprudencia guardada
    datos_jurisprudencia = Jurisprudencia.objects.all()

    # Pasar los datos al contexto
    context = {
        'datos_jurisprudencia': datos_jurisprudencia
    }

    return render(request, 'webTemplates/jurisprudencia/jurisprudencia.html', context)


def consultaMaritima_view(request):
    # Llamar a la función obtener_informacion para obtener y guardar los datos en el modelo
    obtener_informacion()
    print(obtener_informacion())
    # Recuperar los datos del modelo Concesion
    concesiones = Concesion.objects.all()

    # Pasar los datos al contexto
    context = {
        'concesiones': concesiones
    }

    return render(request, 'webTemplates/infoMaritima/infoMaritima.html', context)


# Create your views here.

def Index(request):
    
    return render(request, 'webTemplates/index/index.html', {})
